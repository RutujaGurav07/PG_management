import React, { useState } from 'react'
import { register } from "../api";
import { useNavigate } from "react-router-dom";

const Signup = () => {
    const [email, setEmail] = useState("");
    const [password1, setPassword1] = useState("");
    const [password2, setPassword2] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await register(email, password1, password2);
            alert("Signup Successful");
            navigate("/login"); // Redirect to login page
        } catch (error) {
            alert("Signup Failed");
        }
    };

    return (
        <div>
            <h2>Signup</h2>
            <form onSubmit={handleSubmit}>
                <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                <input type="password" placeholder="Password" value={password1} onChange={(e) => setPassword1(e.target.value)} />
                <input type="password" placeholder="Confirm Password" value={password2} onChange={(e) => setPassword2(e.target.value)} />
                <button type="submit">Signup</button>
            </form>
        </div>
    );
};

export default Signup;
