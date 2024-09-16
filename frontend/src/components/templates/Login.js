import React, { useState } from 'react';
import axios from 'axios';
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput
} from 'mdb-react-ui-kit';
import './Login.css';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate(); // Initialize useNavigate

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/login/', {
        username,
        password
      });

      console.log('Login successful:', response.data);
      // Handle success here, e.g., redirect or save token
      navigate('/dashboard'); // Redirect to dashboard on success
    } catch (err) {
      console.error('Login error:', err);
      if (err.response) {
        const errors = err.response.data.non_field_errors || ['Unknown error occurred'];
        setError(errors.join(' '));
      } else {
        setError('Error connecting to the server.');
      }
    }
  };

  const handleForgotPassword = () => {
    // Handle the forgot password action, e.g., navigate to a password reset page
    navigate('/forgot-password');
  };

  return (
    <MDBContainer fluid className='p-4 background-radial-gradient overflow-hidden'>
      <MDBRow>
        <MDBCol md='6' className='text-center text-md-start d-flex flex-column justify-content-center'>
          <h1 className="my-5 display-3 fw-bold ls-tight px-3 text-primary">
            <span className='text-secondary'>Fint-dev </span>
            BI Analytics Advance Analitics Data Consulting Software Factory<br />
          </h1>
          <p className='px-3 text-primary'>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Eveniet, itaque accusantium odio, soluta, corrupti aliquam
            quibusdam tempora at cupiditate quis eum maiores libero
            veritatis? Dicta facilis sint aliquid ipsum atque?
          </p>
        </MDBCol>
        <MDBCol md='6' className='position-relative'>
          <div id="radius-shape-1" className="position-absolute rounded-circle shadow-5-strong"></div>
          <div id="radius-shape-2" className="position-absolute shadow-5-strong"></div>
          <MDBContainer fluid className='p-4 background-radial-gradient overflow-hidden'>
            <MDBRow className='h-200 d-flex align-items-center justify-content-center'>
              <MDBCol md='6' className='d-flex justify-content-center px-6'>
                <div className="mt-5">
                  <MDBCard className='my-12 bg-glass custom-card'>
                    <MDBCardBody className='p-6'>
                      <div className="text-center">
                        <h1 className="my-3 display-5 fw-bold ls-tight px-3 text-primary">
                          <span className='text-secondary'>Login</span>
                        </h1>
                      </div>
                      <form onSubmit={handleSubmit}>
                        <MDBInput
                          wrapperClass='mb-3'
                          label='Username'
                          id='username'
                          type='text'
                          value={username}
                          onChange={(e) => setUsername(e.target.value)}
                        />
                        <MDBInput
                          wrapperClass='mb-3'
                          label='Password'
                          id='password'
                          type='password'
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                        />
                        {error && <p className="text-danger">{error}</p>}
                        <MDBBtn className='w-100 mb-4' size='md' type='submit'>Login</MDBBtn>
                        <div className="text-center">
                          <MDBBtn
                            color='link'
                            className='p-0'
                            onClick={handleForgotPassword}
                          >
                            ¿Olvidó su contraseña?
                          </MDBBtn>
                        </div>
                      </form>
                    </MDBCardBody>
                  </MDBCard>
                </div>
              </MDBCol>
            </MDBRow>
          </MDBContainer>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
  );
}

export default Login;
