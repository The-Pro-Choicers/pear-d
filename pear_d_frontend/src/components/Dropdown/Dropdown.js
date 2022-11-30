import React from 'react';
import styled from "styled-components";
import './Dropdown.css'

const Dropdown = () => {
  return (
    <div classname="dropdown">
        <button class="dropbtn">Dropdown</button>
        <div class="dropdown-content">
            <a href="#">Link 1</a>
            <a href="#">Link 2</a>
            <a href="#">Link 3</a>
        </div>
    </div>
  )
  
};

export default Dropdown;

