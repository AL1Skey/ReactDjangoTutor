import React, { Component } from "react";
import { useParams } from "react-router-dom";

export default function Room() {
  const { roomCode } = useParams();

  return <h1>{roomCode}</h1>;
}
