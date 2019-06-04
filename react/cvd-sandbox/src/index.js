import React from "react";
import ReactDOM from "react-dom";
// eslint-disable-next-line no-unused-vars
import MUIDataTable from "mui-datatables";
import ldevs from "./ldevs";

import { createMuiTheme } from "@material-ui/core/styles";
import blue from "@material-ui/core/colors/blue";
import yellow from "@material-ui/core/colors/yellow";
// eslint-disable-next-line no-unused-vars
import { MuiThemeProvider } from "@material-ui/core/styles";

import "./index.css";

const theme = createMuiTheme({
  typography: {
    useNextVariants: true
  },
  palette: {
    type: "dark",
    primary: blue,
    secondary: yellow
  },
  overrides: {
    paper: {
      height: "inherit"
    },
    MUIDataTable: {
      responsiveScroll: {
        overflowX: "hidden",
        maxHeight: "none",
        height: "calc(100% - 128px)"
      }
    }
  }
});

function readLdevs() {
  const ldev_data = [];
  for (const ldev of JSON.parse(ldevs).data) {
    ldev_data.push([
      ldev.ldevId,
      ldev.blockCapacity,
      ldev.byteFormatCapacity,
      ldev.attributes.toString(),
      ldev.status,
      ldev.emulationType,
      "raidLevel" in ldev ? ldev.raidLevel : "-",
      "raidType" in ldev ? ldev.raidType : "-"
    ]);
  }
  return ldev_data;
}

// eslint-disable-next-line no-unused-vars
class App extends React.Component {
  render() {
    const columns = [
      "LDEV ID",
      "BlockCapacity",
      "ByteFormatCapacity",
      "Attributes",
      "Status",
      "EmulationType",
      "RaidLevel",
      "RaidType"
    ];

    const data = readLdevs();

    const options = {
      filterType: "multiselect",
      responsive: "scroll",
      selectableRows: "none"
      // resizableColumns: true,
    };

    return (
      <MuiThemeProvider theme={theme}>
        <MUIDataTable
          title={"LDEVS"}
          data={data}
          columns={columns}
          options={options}
        />
      </MuiThemeProvider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("ldevs"));
