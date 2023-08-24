import React from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import RoomView from "./RoomView";
import Room from "./Room";
import { useRoutes } from "react-router-dom";

export default function HomePage() {
  const routes = useRoutes([
    { path: "/", element: <RoomView /> },
    { path: "/create", element: <CreateRoomPage /> },
    { path: "/join", element: <RoomJoinPage /> },
    { path: "/room/:roomCode", element: <Room /> },
  ]);

  return routes; // Kembalikan elemen routes
}
