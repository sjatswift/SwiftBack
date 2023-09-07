import React, { useState } from 'react';

const VehicleJSON = {
  car_makers: [
    {
      name: 'Toyota',
      models: ['Camry', 'Corolla', 'Prius'],
    },
    {
      name: 'Ford',
      models: ['Mustang', 'F-150', 'Explorer'],
    },
    {
      name: 'Volkswagen',
      models: ['Golf', 'Passat', 'Jetta'],
    },
    {
      name: 'Honda',
      models: ['Civic', 'Accord', 'CR-V'],
    },
    {
      name: 'Chevrolet',
      models: ['Silverado', 'Equinox', 'Malibu'],
    },
    {
      name: 'Nissan',
      models: ['Altima', 'Maxima', 'Rogue'],
    },
    {
      name: 'BMW',
      models: ['3 Series', '5 Series', 'X5'],
    },
  ],
};

const VehicleForm: React.FC = () => {
  const [selectedCompany, setSelectedCompany] = useState<string | undefined>(undefined);
  const [selectedModel, setSelectedModel] = useState<string | undefined>(undefined);
   
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/vehicles/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Company: selectedCompany, Model: selectedModel }), // Adjust the field names as per your Django API.
      });

      if (response.ok) {
        // Successful login, you can call a callback function or handle the response accordingly.
        console.log('Submitted successfully');
      } else {
        // Handle errors or display error messages to the user.
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error occurred:', error);
    }
  };



  const handleVehicleCompanyChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedCompany(e.target.value);
    setSelectedModel(undefined); // Reset selected model when the company changes
  };

  const handleVehicleModelChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedModel(e.target.value);
  };

  return (
    <div className="form-control w-full max-w-xs">
      <form onSubmit={handleSubmit}>
        <label className="label">
          <span className="label-text">Vehicle Company</span>
          <select
            onChange={handleVehicleCompanyChange}
            className="select select-bordered w-full max-w-xs"
            value={selectedCompany}
          >
         
            {VehicleJSON.car_makers.map((company) => (
              <option key={company.name} value={company.name}>
                {company.name}
              </option>
            ))}
          </select>
        </label>
        {selectedCompany && (
          <label className="label">
            <span className="label-text">Vehicle Model</span>
            <select
              onChange={handleVehicleModelChange}
              className="select select-bordered w-full max-w-xs"
              value={selectedModel}
            >
              <option value="" disabled>
                Select your Vehicle Model
              </option>
              {VehicleJSON.car_makers
                .find((company) => company.name === selectedCompany)
                ?.models.map((model) => (
                  <option key={model} value={model}>
                    {model}
                  </option>
                ))}
            </select>
          </label>
        )}

    
<div className="form-control w-full max-w-xs">
  <label className="label">
    <span className="label-text">Upload your Vehicle pic</span>
  </label>
  <input type="file" className="file-input file-input-bordered w-full max-w-xs" />
 
</div>

<label className="label">
                <span className="label-text">Registration number</span>
            </label>
            <input type="text" placeholder="Type here" className="input input-bordered w-full max-w-xs" />
         

<button type="submit" className="btn">
          Submit
        </button>
      </form>
    </div>
  );
};

export default VehicleForm;
