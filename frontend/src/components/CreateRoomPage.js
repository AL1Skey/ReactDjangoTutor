import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Button } from "@mui/material";
import { Grid } from "@mui/material";
import { Typography } from "@mui/material";
import { Radio } from "@mui/material";
import { RadioGroup } from "@mui/material";
import { FormControl } from "@mui/material";
import { FormControlLabel } from "@mui/material";
import { FormHelperText } from "@mui/material";
import { TextField } from "@mui/material";
export default class CreateRoomPage extends Component {
  defaultVotes = 2;

  constructor(props) {
    super(props);
    //Defaut state
    this.state = {
      can_pause: true,
      skip_vote: this.defaultVotes,
    };
    // Initialize handler with bind so it can be called inside some method
    this.handleRoomCreation = this.handleRoomCreation.bind(this); // (this) refer of handleRoomCreation
    this.handleVotesChange = this.handleVotesChange.bind(this);
    this.handleCanPauseChange = this.handleCanPauseChange.bind(this);
  }

  handleVotesChange(e) {
    this.setState({
      skip_vote: e.target.value,
    });
  }
  handleCanPauseChange(e) {
    this.setState({
      can_pause: e.target.value === "true" ? true : false,
    });
  }
  handleRoomCreation() {
    const request = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        can_pause: this.state.can_pause,
        skip_vote: this.state.skip_vote,
      }),
    };
    fetch("/api/create-room", request)
      .then((response) => response.json())
      .then((data) => console.log(data));
  }

  render() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            Createing a Roomn
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl component="fieldset">
            <FormHelperText>
              <div align="center">
                Guest Control PlayBack State or SOmething
              </div>
            </FormHelperText>
            <RadioGroup
              row
              defaultValue="True"
              onChange={this.handleCanPauseChange}
            >
              <FormControlLabel
                value="True"
                control={<Radio color="primary" />}
                label="Play/Pause"
                labelPlacement="bottom"
              />
              <FormControlLabel
                value="False"
                control={<Radio color="secondary" />}
                label="No Control"
                labelPlacement="bottom"
              />
            </RadioGroup>
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="number"
              defaultValue={this.defaultVotes}
              inputProps={{
                min: 2,
              }}
              onChange={this.handleVotesChange}
            />
            <FormHelperText>
              <div align="center">Votes Require to skip songs</div>
            </FormHelperText>
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            color="primary"
            variant="contained"
            onClick={this.handleRoomCreation}
          >
            Create a Room
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button color="secondary" variant="contained" to="/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}
