import React from 'react';
import PredictView from '../../src/views/PredictView';
import Main from '../../src/layouts/Main';
import WithLayout from '../../src/WithLayout';
//creating index.js for pneumocheck for predict view
const Predict = () => {
  return (
    <WithLayout
      component={PredictView}
      layout={Main}
    />
  )
};

export default Predict;
