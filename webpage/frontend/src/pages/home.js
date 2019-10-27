import React, { Component } from 'react';
import axios from 'axios'
import { Container, Button } from '@material-ui/core';
import Paper from '@material-ui/core/Paper';
import TextField from '@material-ui/core/TextField';


class SearchField extends Component {
  constructor(props) {
    super(props)
  }

  postValue(value) {
    axios.post(process.env.REACT_APP_API_URL)
      .then(res => {
        console.log(res)
      }
      )
  }

  handleChange(event) {
    this.postValue(event.target.value)
  }

  render() {
    return (
      <TextField
        id="outlined-full-width"
        onChange={(e) => { this.handleChange(e) }}
        label="Search"
        fullWidth
        margin="normal"
        variant="outlined"
      />
    )
  }
}

class Home extends Component {
  render() {
    return (
      <Container>
        <SearchField />
      </Container>
    );
  }
}

export default Home;