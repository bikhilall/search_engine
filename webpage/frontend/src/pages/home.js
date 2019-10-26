import React, { Component } from 'react';
import { Container, Button } from '@material-ui/core';
import Paper from '@material-ui/core/Paper';
import TextField from '@material-ui/core/TextField';


class Home extends Component {
  render() {
    return (
      <Container>
        <TextField
          id="outlined-full-width"
          label="Search"
          fullWidth
          margin="normal"
          variant="outlined"
        />
      </Container>
    );
  }
}

export default Home;