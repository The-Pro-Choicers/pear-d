import React from 'react'
import { getAll } from '../actions/restaurant';
import { connect } from 'react-redux';
import Dropdown from '../components/Dropdown/Dropdown';

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
        <Dropdown/>
        <button type="submit">get all data</button>
      </form>
        
    </>
  )
}

export default connect( null, { getAll })(Restaurants);