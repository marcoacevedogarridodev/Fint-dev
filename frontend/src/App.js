import React from 'react';
import {
  MDBBtn,
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBInput
}
from 'mdb-react-ui-kit';
import './App.css'; 

function App() {
  return (
    <MDBContainer fluid className='p-4 background-radial-gradient overflow-hidden'>

      <MDBRow>

        <MDBCol md='6' className='text-center text-md-start d-flex flex-column justify-content-center'>

          <h1 className="my-5 display-3 fw-bold ls-tight px-3" style={{color: 'hsl(218, 81%, 85%)'}}>
            <span style={{color: 'hsl(218, 191%, 25%)'}}>Fint-dev </span>
            BI Analytics Advance Analitics Data Consulting Software Factory<br />
          </h1>

          <p className='px-3' style={{color: 'hsl(218, 81%, 85%)'}}>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Eveniet, itaque accusantium odio, soluta, corrupti aliquam
            quibusdam tempora at cupiditate quis eum maiores libero
            veritatis? Dicta facilis sint aliquid ipsum atque?
          </p>

        </MDBCol>

        <MDBCol md='6' className='position-relative'>

          <div id="radius-shape-1" className="position-absolute rounded-circle shadow-5-strong"></div>
          <div id="radius-shape-2" className="position-absolute shadow-5-strong"></div>

          <MDBContainer fluid className='p-4 background-radial-gradient overflow-hidden custom-container'>
          <MDBRow className='h-200 d-flex align-items-center justify-content-center'>
            <MDBCol md='6' className='d-flex justify-content-center'>
              <div className="mt-5"> 
                <MDBCard className='my-12 bg-glass'>
                  <MDBCardBody className='p-6'>
                    <div className="text-center">
                      <h1 className="my-3 display-5 fw-bold ls-tight px-3" style={{color: 'hsl(218, 81%, 85%)'}}>
                        <span style={{color: 'hsl(218, 191%, 55%)'}}>Login</span>        
                      </h1>
                    </div>

                    <MDBInput wrapperClass='mb-4' label='Email' id='form3' type='email'/>
                    <MDBInput wrapperClass='mb-4' label='Password' id='form4' type='password'/>

                    <MDBBtn className='w-100 mb-4' size='md'>Login</MDBBtn>

                    <div className="text-center">
                      <p>¿Olvidó su contraseña?</p>
                    </div>
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

export default App;