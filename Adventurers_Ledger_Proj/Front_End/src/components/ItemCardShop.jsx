import React from "react";
import Buy_or_Sell_Item from "../services/BuySellLogic";

const ItemCardShop = ({ item }) => {

    // Function to handle buying or selling an item
    const handleBuyOrSell = (action, item) => {
        Buy_or_Sell_Item(action, item);
    }

  return (
    <div className="item bg-yellow-100 p-4 rounded shadow w-64">
      <strong className="text-yellow-800 block mb-2 text-center">{item.item.name}</strong>
      <p className="text-sm text-gray-700 line-clamp-3">{item.item.description ? `Description: ${item.item.description}`:null}</p>
      <p className=" font-semibold text-yellow-900">Price: {item.item.cost_amount} {item.item.cost_unit}</p>
      <div className="flex justify-center mt-2">
      <button onClick={() => handleBuyOrSell('buy', item.item)} className=" bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600 transition-colors">Buy</button>
      <button onClick={() => handleBuyOrSell('sell', item.item)} className=" bg-yellow-300 text-yellow-800 px-4 py-2 rounded hover:bg-yellow-400 transition-colors">Sell</button>
      </div>
    </div>
  );
};

export default ItemCardShop;
