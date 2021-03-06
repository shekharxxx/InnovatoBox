import React from "react";
import "./App.css";
//import HomePage from "./HomePage";
 import LoginRegister from "./LoginRegister";

const App = () => {
  return (
    //BEM class naming convention
    <div className="app">
        { <LoginRegister/> }
        {/*<HomePage/>*/}
    </div>   
  );
};

export default App;
