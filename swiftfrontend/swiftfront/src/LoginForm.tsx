import React, { useState } from 'react';

interface LoginFormProps {
  onLoginSuccess: () => void;
}

const LoginForm: React.FC<LoginFormProps> = ({ onLoginSuccess }) => {
  const [phoneNumber, setPhoneNumber] = useState<string>('');
  const [password, setPassword] = useState<string>('');

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/api/auth/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ phone: phoneNumber, password: password }), // Adjust the field names as per your Django API.
      });

      if (response.ok) {
        // Successful login, you can call a callback function or handle the response accordingly.
        console.log('Login successful');
        onLoginSuccess();
      } else {
        // Handle errors or display error messages to the user.
        console.error('Login failed');
      }
    } catch (error) {
      console.error('Error occurred:', error);
    }
  };

  return (
    <div className="form-control w-full max-w-xs">
      <form onSubmit={handleSubmit}>
        <label className="label">
          <span className="label-text">Phone Number</span>
        </label>
        <input
          type="text"
          placeholder="Type here"
          className="input input-bordered w-full max-w-xs"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
        />

        <label className="label">
          <span className="label-text">Password</span>
        </label>
        <input
          type="password"
          placeholder="Type here"
          className="input input-bordered w-full max-w-xs"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="submit" className="btn">
          Submit
        </button>
      </form>
    </div>
  );
};

export default LoginForm;
