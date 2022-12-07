
import React, { useState, useEffect } from 'react';
import { getAll, filterRestaurants, addFav, removeFav } from '../actions/restaurant';
import { connect } from 'react-redux';
import styled from "styled-components";
import { AiFillStar } from 'react-icons/ai'
import { FaDirections } from 'react-icons/fa'
import { motion } from 'framer-motion'

const Restaurants = ({ getAll, filterRestaurants, addFav, removeFav }) => {
  const [restaurants, setRestaurants] = useState([]);
  const [food, setFood] = useState(0);
  const [env, setEnv] = useState(false);
  const [min, setMin] = useState(false);
  const [phil, setPhil] = useState(false);
  const [price, setPrice] = useState(0);
  const [pressed, setPressed] = useState(true);

  useEffect(() => {
    
    getAll()
    .then(function(result) {
        console.log(result);
        setRestaurants(result);
    });
    
  }, [])

  const onSubmit = e => {
    console.log("button clicked");
     e.preventDefault();
     filterRestaurants(food, env, phil, min, price).then(function(result) {
         console.log(result);
         setRestaurants(result);
     })
  }

  const addFavorite = (e, rest_id) => {
    setPressed(!pressed)
    console.log("id is", rest_id);
     e.preventDefault();
     if (pressed) {
      addFav(rest_id);
      console.log("Favorited Restaurant w/ ID: ", rest_id);
     }
     else {
      removeFav(rest_id);
      console.log("Unfavorited Restaurant w/ ID: ", rest_id);
     }
     
  }

return (
  <>
    <Wrap>
      <div>Restaurant Data</div>
      <Wrapper>
      <Dropdown>
          <button className="dropbtn" name="food" id="food_pref">food type</button>
          <div className="dropdown-content">
            <a name="food" onClick={() => setFood(0)}>fast food</a>
            <a name="food" onClick={() => setFood(1)}>drinks/deserts</a>
            <a name="food" onClick={() => setFood(2)}>american</a>
            <a name="food" onClick={() => setFood(3)}>asian</a>
            <a name="food" onClick={() => setFood(4)}>hispanic</a>
            <a name="food" onClick={() => setFood(5)}>indian</a>
            <a name="food" onClick={() => setFood(6)}>italian</a>
            <a name="food" onClick={() => setFood(7)}>mediterranean</a>
            <a name="food" onClick={() => setFood(8)}>seafood</a>
          </div>      
      </Dropdown>
      <Dropdown>
          <button className="dropbtn" name="price" id="price-level">price level</button>
            <div className="dropdown-content">
              <a name="price" onClick={() => setPrice(1)}>$</a>
              <a name="price" onClick={() => setPrice(2)}>$$</a>
              <a name="price" onClick={() => setPrice(3)}>$$$</a>
              <a name="price" onClick={() => setPrice(4)}>$$$$</a>
            </div>
      </Dropdown>
      <Dropdown>
         <button className="dropbtn">social good</button>
         <div className="dropdown-content">
          <a type="checkbox" name="env" onClick={() => setEnv(!env)}>eco-concious</a>
          <a name="min" onClick={() => setMin(!min)}>minority owned</a>
          <a name="ph" onClick={() => setPhil(!phil)}>philanthropist</a>
         </div>
      </Dropdown>
      </Wrapper>
      <button className="apply" onClick={e => onSubmit(e)}>apply</button>
      <RestaurantBubble>
      { restaurants.map(restaurant => (
          <div className="item" key={restaurant.id}>
          <div className="rest-img app__flex">
            <div />
            <motion.div
                whileHover={{ opacity: [0, 1] }}
                transition={{ duration: 0.25, ease: 'easeInOut', staggerChildren: 0.5 }}
                className="rest-hover app__flex"
              >
                <a href={restaurant.url} target="_blank" rel="noreferrer">

                  <motion.div
                    whileInView={{ scale: [0, 1] }}
                    whileHover={{ scale: [1, 0.90] }}
                    transition={{ duration: 0.25 }}
                    className="app__flex"
                  >
                    <FaDirections />
                  </motion.div>
                </a>
              </motion.div>
          </div>
          <div className="rest-content app__flex">
            <h4>{restaurant.name}</h4>
            <p className="p-text app__flex" style={{ marginTop: 10 }}>Address:   {restaurant.address}</p>
            <p className="p-text" style={{ marginTop: 10 }}>Price Level:   {restaurant.price_level}</p>
            <p className="p-text" style={{ marginTop: 10 }}>Rating:   {restaurant.rating}</p>
            <div className="icon">
              <AiFillStar onClick={e => addFavorite(e, restaurant.id)}/>
            </div>
            <div className="rest-tag app__flex">
              <p className="p-text" style={ {color: "black"}}>{restaurant.food_category}</p>
            </div>
          </div>
        </div>
      ))}
      </RestaurantBubble>
    </Wrap>
  </>
  
)
}

const Wrap = styled.div`
  height: 100vh;
  width: 100%;
  background: linear-gradient(-45deg, #e2e1cd, #dcd893, #f4f0a0, #d4d1a1);
	background-size: 300% 300%;
	animation: gradient 20s ease infinite;
  overflow: auto;
`;

const Wrapper = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  font-family: 'peard_font' !important;
`;


const Dropdown = styled.div`

  position: relative;
  display: inline-block;
  margin-left: 30px;

  &:hover .dropdown-content {
    display: block;
    cursor: pointer;
  }

  &:hover .dropbtn {
    display: block;
  }

  .dropbtn {
    width: 6.5rem;
    height: 2.2rem;
    margin: 0.5rem;
    border: none;
    border-radius: 0.5rem;
    background-color: #96aa56;
    color: white;
    font-family: 'peard_font', sans-serif;
    transition: all 500ms ease;

    &:hover {
      cursor: pointer;
    }
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;

    a {
      color: black;
      padding: 12px 16px;
      text-decoration: none;
      display: block; 
      border-radius: 10px; 
      
       &:hover {
        background-color: #ddd;
        cursor: pointer;
       }
    }
  }
  

`;

const RestaurantBubble = styled.div`

  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;

  .rest-hover {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);

    border-radius: 0.5rem;
    opacity: 0;
    transition: all 0.3s ease;

    div {
      display: flex;
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background-color: rgba(0, 0, 0, 0.5);
      color: #fff;
      align-items: center;

      margin: 1rem;
      font-family: var(--font-base);
      font-weight: 800;
      cursor: pointer;
      transition: all 0.3s ease;

      svg {
        width: 80%;
        height: 80%;
        color: white;
      }
  }
}

  .icon {
    display: flex;
    flex-direction: row;
    cursor: pointer;
  }
  
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
    
      div {
        width: 100%;
        height: 100%;
        border-radius: 0.5rem;
        background-colorL white;
        cursor: pointer;
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
      height: 30%;
      width: 30%;
      position: absolute;
      font-weight: bold;
      padding: 0.5rem 1rem;
      border-radius: 10px;
      background-color: ##96aa56;
      top: -25px;           
  }

`;
export default connect( null, { getAll, filterRestaurants, addFav, removeFav })(Restaurants);