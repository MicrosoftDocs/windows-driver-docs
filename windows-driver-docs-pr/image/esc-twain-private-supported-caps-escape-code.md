---
title: ESC_TWAIN_PRIVATE_SUPPORTED_CAPS Escape Code
description: ESC_TWAIN_PRIVATE_SUPPORTED_CAPS Escape Code
ms.assetid: 99b9f180-018b-47c4-ab8d-dc037e3f637a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS Escape Code





In order to determine private TWAIN-supported capabilities, a TWAIN application notifies the TWAIN compatibility layer, which then sends the ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS escape code to the WIA driver's [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) method. The following pseudocode implementation of the **Escape** method demonstrates how it should respond to the ESC\_TWAIN\_PRIVATE\_SUPPORTED\_CAPS escape code to report private TWAIN-support capabilities.

**Note**   The **Escape** method in this example is the same as the one shown in [ESC\_TWAIN\_CAPABILITY Escape Code](esc-twain-capability-escape-code.md), although the focus of each sample is a different escape code.

 

```cpp
STDMETHODIMP CWIADevice::Escape(STI_RAW_CONTROL_CODE EscapeFunction,
  LPVOID               lpInData,
  DWORD                cbInDataSize,
  LPVOID               pOutData,
  DWORD                dwOutDataSize,
  LPDWORD              pdwActualData)
{
  //
  // Only process EscapeFunction codes that are known to your driver.
  // Any application can send escape calls to your driver using the
  // IWiaItemExtras interface Escape() method call.  The driver must
  // be prepared to validate all incoming calls to Escape().
  //

  //
  // Because this driver does not support any escape functions, it will
  // reject all incoming EscapeFunction codes.
  //
  // If your driver supports an EscapeFunction, then add your function
  // code to the switch statement, and set hr = S_OK. This will allow
  // the function to continue to the incoming/outgoing buffer
  // validation.
  //

  HRESULT hr = E_NOTIMPL;
  switch(EscapeFunction) {
  case ESC_TWAIN_PRIVATE_SUPPORTED_CAPS: // processing TWAIN supported caps Escapecode
     hr = S_OK;
     break;
  default:
     break;
  }

  //
  // If an EscapeFunction code is supported, then first validate the
  // incoming and outgoing buffers.
  //

  if(S_OK == hr) {

     //
     // Validate the incoming data buffer.
     //

     if(IsBadReadPtr(lpInData,cbInDataSize)) {
         hr = E_UNEXPECTED;
     }

     //
     // If the incoming buffer is valid, proceed to validate the
     // outgoing buffer.
     //

     if(S_OK == hr) {
         if(IsBadWritePtr(pOutData,dwOutDataSize)) {
             hr = E_UNEXPECTED;
         } else {

             //
             // Validate the outgoing size pointer.
             //

             if(IsBadWritePtr(pdwActualData,sizeof(DWORD))) {
                 hr = E_UNEXPECTED;
             }
        }
     }

     //
     // Now that buffer validation is complete, proceed to process the
     // proper EscapeFunction code.
     //

     if(S_OK == hr) {

       //
       // Only process a validated EscapeFunction code, and buffers.
       //

       if(EscapeFunction == ESC_TWAIN_PRIVATE_SUPPORTED_CAPS) {

           //
           // Process a TWAIN supported capabilities message.
           //

           // Check the lpInData buffer for the number of bytes
           // of the capability array.
           //
           // 1. Create variable of type LONG*, initializing it
           //    to the value in lpInData.
           // 2. Dereference this variable to obtain the size, in
           //    bytes, of the private TWAIN capability array.

           LONG *pSupportedCapsSize = NULL;
           pSupportedCapsSize = (LONG*)lpInData;

           if(pSupportedCapsSize) {
               LONG lNumBytes = *pSupportedCapsSize;

                // lNumBytes determines the operation to perform.

               if(lNumBytes == 0) {
                // If lNumBytes is zero:
                // a. Create a variable of type LONG*, and
                //    initialize it to the value in pOutData.
                // b. Dereference this variable, and set the size,
                //    in bytes, of the private TWAIN capability array.
                //  c. Set *pchActualData to sizeof(LONG).
                //  d. Set the HRESULT to S_OK, and return.

                  LONG *pCapArraySize = (LONG*)pOutData;
                  *pCapArraySize = (NUM_PRIVATE_TWAIN_CAPS * sizeof(LONG));
                  *pdwActualData = sizeof(LONG);
                   hr = S_OK;
               } else if(lNumBytes > 0) {
                  // If lNumBytes is positive:
                  //  a. Create a variable of type LONG*, and
                  //     initialize it to the value in pOutData.
                  //  b. Dereference this variable, and set each
                  //     capability ID of the private TWAIN capability
                  //     array.
                  //  c. Set *pchActualData to the size, in bytes, of
                  //     the total capability array.
                  //  d. Set the HRESULT to S_OK, and return.

                   LONG *pCapArray = (LONG*)pOutData;
                   pCapArray[0] = ICAP_MY_PRIVATE_CAP1;
                   pCapArray[1] = ICAP_MY_PRIVATE_CAP2;
                   pCapArray[2] = ICAP_MY_PRIVATE_CAP3;
                   pCapArray[3] = ICAP_MY_PRIVATE_CAP4;
                   pCapArray[4] = ICAP_MY_PRIVATE_CAP5;
                   *pdwActualData = (NUM_PRIVATE_TWAIN_CAPS * sizeof(LONG));
                   hr = S_OK;
               } // if (lNumBytes > 0)
           } // if (pSupportedCapsSize)
       }
     }
  }

  //
  // If your driver will not support this entry point, then
  // it must return E_NOTIMPL (error, not implemented).
  //

  return hr;
}
```

 

 




