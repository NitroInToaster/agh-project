import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../../config/navigationLinks";
import { UserNav } from "../CustomersPage/components/UserNav";
import { useState } from "react";
import useAlert from "./components/useAlert";
import { AlertProvider } from "./components/AuthContext";

export const AddCustomerPage = () => {
  
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");

  const getName = (event) => {
    setName(event.target.value)};

  const getSurname = (event) => {
      setSurname(event.target.value)};

  const getEmail = (event) => {
    setEmail(event.target.value)
  };

  const getPhoneNumber = (event) => {
    setPhoneNumber(event.target.value)};

  const submitFormHandler = async (e) => {
    e.preventDefault();

    
    
    const customer = {
      name: name,
      surname: surname,
      email: email,
      phone_number: phoneNumber
    };
    console.log(customer);

    const response = await fetch("http://127.0.0.1:8000/customers/", {
      method: "POST",
      body: JSON.stringify(customer),
      headers: {
        "Content-Type": "application/json",
      },
    });

    console.log(response);
  };




  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex"></div>
      </div>
      <form onSubmit={submitFormHandler} className="addCustomer">
        <label>Name</label>
        <input onChange={getName} value={name} type="text" placeholder="Name"></input>
        <label>Surname</label>
        <input onChange={getSurname} value={surname} type="text" placeholder="Surname"></input>
        <label>Email</label>
        <input onChange={getEmail} value={email} type="text" placeholder="Email"></input>
        <label>Phone number</label>
        <input onChange={getPhoneNumber} value={phoneNumber} type="text" placeholder="Phone number"></input>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};
