import axios from 'axios';

export const getAll = () => async dispatch => {

    console.log("in get all");
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    try {
        
        const res = await axios.get('http://127.0.0.1:8000/api/profile/myprofile/view/', config);

        dispatch({
            payload: res.data
        });
        console.log(res.data);
  

    } catch (err) {

        console.log(err);
        dispatch({
        });
    }
};