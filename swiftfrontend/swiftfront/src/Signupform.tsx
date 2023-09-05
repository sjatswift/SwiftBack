
const Signupform = () => {
    return (
        <div className="form-control w-full max-w-xs">
            <label className="label">
                <span className="label-text">What is your name?</span>
            </label>
            <input type="text" placeholder="Type here" className="input input-bordered w-full max-w-xs" />
         

            <label className="label">
                <span className="label-text">Email Address</span>
            </label>
            <input type="email" placeholder="Type here" className="input input-bordered w-full max-w-xs" />
         

            <label className="label">
                <span className="label-text">Phone Number</span>
            </label>
            <input type="phone" placeholder="Type here" className="input input-bordered w-full max-w-xs" />
         

            <div className="form-control flex">
  <label className="label cursor-pointer">
    <span className="label-text">Male</span> 
    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked />
  </label>

  <label className="label cursor-pointer">
    <span className="label-text">Female</span> 
    <input type="radio" name="radio-10" className="radio checked:bg-red-500" checked />
  </label>
</div>


<select className="select select-bordered w-full max-w-xs">
  <option disabled selected>Select your Role</option>
  <option>Ride Taker</option>
  <option>Ride Giver</option>
</select>


<select className="select select-bordered w-full max-w-xs">
  <option disabled selected>Select your College</option>
  <option>SPIJM</option>
  <option>Reva University</option>
</select>

<div className="form-control w-full max-w-xs">
  <label className="label">
    <span className="label-text">Upload your ID card pic</span>
  </label>
  <input type="file" className="file-input file-input-bordered w-full max-w-xs" />
 
</div>


<div className="form-control w-full max-w-xs">
  <label className="label">
    <span className="label-text">Upload your Profile pic</span>
  </label>
  <input type="file" className="file-input file-input-bordered w-full max-w-xs" />
 
</div>


<div className="form-control w-full max-w-xs">
  <label className="label">
    <span className="label-text">Upload your License pic</span>
  </label>
  <input type="file" className="file-input file-input-bordered w-full max-w-xs" />
 
</div>

<button className="btn">Submit</button>

        </div>
    )
}

export default Signupform