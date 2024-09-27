import React from 'react';
import { login } from '../services/api';

const Login = () => {
 return (
  <button onClick={login}>Login with Reddit</button>
 );
};

export default Login;
