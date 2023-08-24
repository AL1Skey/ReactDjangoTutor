import { Button } from "@mui/material";
import React, { Component } from "react";

export default class RoomView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      roomModel: [],
    };
  }

  componentDidMount() {
    //Add room model after fetch are finished
    const request = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    fetch("/api/room", request)
      .then((response) => response.json())
      .then((data) => this.setState({ roomModel: data }));
  }

  //   handleRoomView() {
  //     const request = {
  //       method: "GET",
  //       headers: { "Content-Type": "application/json" },
  //     };
  //     console.log(this.state.roomModel);
  //   }

  render() {
    return (
      //   <Button color="primary" variant="contained" onClick={this.handleRoomView}>
      //     TEST
      //   </Button>
      <ul>
        {this.state.roomModel.map((room) => (
          <li key={room.id}>{room.host}</li>
        ))}
      </ul>
    );
  }
}
