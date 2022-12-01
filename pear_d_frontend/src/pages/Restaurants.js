import React, { useState } from 'react';
import { getAll } from '../actions/restaurant';
import { connect } from 'react-redux';
import styled from "styled-components";

const Restaurants = ({ getAll }) => {
    const [restaurants, setRestaurants] = useState([]);

    const onSubmit = e => {
       console.log("button clicked");
        e.preventDefault();
        getAll()
        .then(function(result) {
            console.log(result);
            setRestaurants(result);
        });
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
                <option value={4}>$$$$</option>
            </select>
        </Dropdown>
        <Dropdown>
            <select className="drop" name="social" id="social-good">
                <option value="default" disabled selected>social good</option>
                <option value={1}>eco-concious</option>
                <option value={1}>minority owned</option>
                <option value={1}>philanthropist</option>
            </select>
        </Dropdown>
        </Wrapper>
        <button type="submit">apply</button>
      </form>
      { restaurants.map(restaurant => (
        <RestaurantBubble>
            <div className="item" key={restaurant.id}>
            <div className="rest-img app__flex">
              <img src={restaurant.photo_ref} alt={restaurant.name} />
            </div>
            <div className="rest-content app__flex">
              <h4>{restaurant.name}</h4>
              <p className="p-text app__flex" style={{ marginTop: 10 }}>Address:   {restaurant.address}</p>
              <p className="p-text" style={{ marginTop: 10 }}>Price Level:   {restaurant.price_level}</p>
              <p className="p-text" style={{ marginTop: 10 }}>Rating:   {restaurant.rating}</p>              
              <a href={restaurant.url} className="p-text" style={{ marginTop: 10 }}>Let's Go!</a>
              <div className="rest-tag app__flex">
                <p className="p-text" style={ {color: "black"}}>{restaurant.food_category}</p>
              </div>
            </div>
          </div>
        </RestaurantBubble>
      ))}
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

const RestaurantBubble = styled.div`

    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;

    .p-text {
        font-size: 0.8rem;
        text-align: left;
        color: var(--gray-color);
        line-height: 1.5;
      
        @media screen and (min-width: 2000px) {
          font-size: 1.75rem;
        }
    }

    .app__flex {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .item {
        width: 270px;
        flex-direction: column;

        margin: 2rem;
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #96aa56;
        color: #fff;

        cursor: pointer;
        transition: all 0.3s ease;

        &:hover {
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);
        }

        @media screen and (min-width: 2000px) {
        width: 470px;
        padding: 1.25rem;
        border-radius: 0.75rem;
        }

        @media screen and (max-width: 300px) {
        width: 100%;
        margin: 1rem;
        }
    }

    .rest-img {
        width: 100%;
        height: 230px;
      
        position: relative;
      
        img {
          width: 100%;
          height: 100%;
          border-radius: 0.5rem;
          object-fit: cover;
        }
      
        @media screen and (min-width: 2000px) {
          height: 350px;
        }  
    }
 
    .rest-content {
        padding: 0.5rem;
        width: 100%;
        position: relative;
        flex-direction: column;
      
        h4 {
          margin-top: 1rem;
          line-height: 1.5;
      
          @media screen and (min-width: 2000px) {
            margin-top: 3rem;
          }       
    }

    .rest-tag {
        position: absolute;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        background-color: #fff;
        top: -35px;           
    }

`;

export default connect( null, { getAll })(Restaurants);