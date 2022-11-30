import React from 'react';
import { getAll } from '../actions/restaurant';
import { connect } from 'react-redux';
import styled from "styled-components";

const Restaurants = ({ getAll }) => {

    const onSubmit = e => {
       console.log("button clicked");
        e.preventDefault();
        getAll();

    }

  return (
    <>
      <form onSubmit={e => onSubmit(e)}>
        <div>Restaurant Data</div>
        <Wrapper>
        <Dropdown>
            <select className="drop" name="food" id="food-type">
                <option value="default" disabled selected>food type</option>
                <option value={0}>fast food</option>
                <option value={1}>drinks/desert</option>
                <option value={2}>american</option>
                <option value={3}>asian</option>
                <option value={4}>hispanic</option>
                <option value={5}>indian</option>
                <option value={6}>italian</option>
                <option value={7}>mediterranean</option>
                <option value={8}>seafood</option>
            </select>
        </Dropdown>
        <Dropdown>
            <select className="drop" name="price" id="price-level">
                <option value="default" disabled selected>price level</option>
                <option value={1}>$</option>
                <option value={2}>$$</option>
                <option value={3}>$$$</option>
            </select>
        </Dropdown>
        <Dropdown>
            <select className="drop" name="social" id="social-good">
                <option value="default" disabled selected>social good</option>
                <option value={1}>eco-concious</option>
                <option value={2}>minority owned</option>
                <option value={3}>philanthropist</option>
            </select>
        </Dropdown>
        </Wrapper>
        <button type="submit">get all data</button>
      </form>
        
    </>
  )
}

const Wrapper = styled.div`

    display: flex;
    flex-direction: row;
    align-items: center;
    font-family: 'peard_font' !important;
`;

const Dropdown = styled.div`

    position: relative;

    .drop {
       width: 100px;
       height: 30px;
       border-radius: 10px;
       color: white;
       background-color: #96aa56;
       border: none;
       margin: 30px;
    }
    

`;

export default connect( null, { getAll })(Restaurants);