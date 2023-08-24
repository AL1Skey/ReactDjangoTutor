const path = require("path");
const webpack = require("webpack");

module.exports = {
  cache: false,
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/bundle"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js?$/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-react"],
          plugins: ["@emotion"],
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
