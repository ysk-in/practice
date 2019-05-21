import React from "react";
import ReactDOM from "react-dom";
// eslint-disable-next-line no-unused-vars
import MUIDataTable from "mui-datatables";
import ldevs from "./ldevs";

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
      responsive: "scroll"
    };

    return (
      <MUIDataTable
        title={"LDEVS"}
        data={data}
        columns={columns}
        options={options}
      />
    );
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
