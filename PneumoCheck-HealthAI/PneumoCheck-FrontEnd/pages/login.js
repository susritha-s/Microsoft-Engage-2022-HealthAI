import React from 'react';
import LoginView from '../src/views/LoginView';
import Main from '../src/layouts/Main';
import WithLayout from '../src/WithLayout';
// creating login.js for LoginView -Pneumochek.

const Login = () => {
  return (
    <WithLayout
      component={LoginView}
      layout={Main}
    />
  )
};

export default Login;
