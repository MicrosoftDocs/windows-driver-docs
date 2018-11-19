---
title: ESC_TWAIN_CAPABILITY Escape Code
description: ESC_TWAIN_CAPABILITY Escape Code
ms.assetid: 3fd3f03b-ea72-4151-a19c-3e71cf3193fa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ESC\_TWAIN\_CAPABILITY Escape Code





To carry out a capability operation on a private TWAIN capability, a TWAIN application notifies the TWAIN compatibility layer, which then calls the WIA driver's [**IStiUSD::Escape**](https://msdn.microsoft.com/library/windows/hardware/ff543815) method, passing the ESC\_TWAIN\_CAPABILITY escape code. The pseudocode in the following example demonstrates how the **Escape** method should be implemented, and how it should respond to the escape code.

```cpp
STDMETHODIMP CWIADevice::Escape(STI_RAW_CONTROL_CODE EscapeFunction,
  LPVOID  lpInData,
  DWORD  cbInDataSize,
  LPVOID  pOutData,
  DWORD  dwOutDataSize,
  LPDWORD  pdwActualData)
{
 //  
  // Only process EscapeFunction codes that are known to your driver.
  // Any application can send escape calls to your driver using the
  // IWiaItemExtras interface Escape() method call. The driver must
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

  HRESULT hr = E_NOTIMPL;
  switch(EscapeFunction) {
  case ESC_TWAIN_CAPABILITY:  // processing the TWAIN capability Escapecode
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

       if(EscapeFunction == ESC_TWAIN_CAPABILITY) {

           //
           // Process a TWAIN capability message.
           //

           // Collect the lpInData and pOutData headers.
           //
           // 1. Create two TWAIN_CAPABILITY pointers in which
           //    to store the addresses in lpInData and pOutData.
           // 2. Set these local pointers to the addresses in
           //    lpInData and pOutData.
           // 3. Use these local pointers to access the
           //    members of the TWAIN_CAPABILITY structures.

           TWAIN_CAPABILITY *pInHeader  = NULL;
           TWAIN_CAPABILITY *pOutHeader = NULL;

           pInHeader  = (TWAIN_CAPABILITY*)lpInData;
           pOutHeader = (TWAIN_CAPABILITY*)pOutData;

           if(pInHeader && pOutHeader) {
         // Check the headers to determine the operation to perform.

               switch(pInHeader->lCapID) {
               case ICAP_MY_PRIVATE_CAP1:
                  {
                      // Check lMSG to determine which TWAIN
                      // message/operation is being requested.
                      switch(pInHeader->lMSG) {
                       case MSG_GETCURRENT: // Return the current value.
                       case MSG_GETDEFAULT: // Return the default value.
                       case MSG_GET:        // Return the valid values.
                           {
                               // Check lDataSize to determine
                               // which operation to perform.
                               if(pInHeader->lDataSize == 0) {
                         // If lDataSize is zero:
                         // a. Set pOutHeader->lDataSize to the size
                         //    in bytes needed to store the entire
                         //    TWAIN capability data.
                         // b. Set *pchActualData to the size of
                         //    a TWAIN_CAPABILITY header.
                         // c. Set the TWAIN return codes,
                         //    pOutHeader->lRC and pOutHeader->lCC.
                         // d. Set the HRESULT to S_OK, and return.

                                 pOutHeader->lDataSize = sizeof(TW_ENUMERATION) +
                                (sizeof(TW_UINT32) * 3);
                                *pdwActualData  = sizeof(TWAIN_CAPABILITY);
                                 pOutHeader->lRC = TWRC_SUCCESS;
                                 pOutHeader->lCC = TWCC_SUCCESS;
                                 hr = S_OK;
                             } else if(pInHeader->lDataSize > 0) {
                     // If lDataSize is positive:
                     //   a. Fill the pOutHeader->Data member with
                     //      the TWAIN capability data.
                     //      (This is the container and data only).
                     //   b. Set pOutHeader->lConType to the type of
                     //      TWAIN container used.
                     //   c. Set pOutHeader->lDataSize to
                     //      (size of the TWAIN container + size of
                     //      the TWAIN container data).
                     //   d. Set *pchActualData to
                     //      (size of the TWAIN container + size of
                     //      the TWAIN container data +
                     //      size of the TWAIN_CAPABILITY header).
                     //   e. Set the TWAIN return codes,
                     //      pOutHeader->lRC and pOutHeader->lCC.
                     //   f. Set the HRESULT to S_OK, and return.
                                 pEnumeration = (TW_ENUMERATION*)pOutHeader->Data;
                                 if(pEnumeration) {
                                     pEnumeration->ItemType     = TWTY_UINT32;
                                     pEnumeration->NumItems     = 3;
                                     pEnumeration->CurrentIndex = 0;
                                     pEnumeration->DefaultIndex = 1;

                                     TW_UINT32 *pData = (TW_UINT32*)pEnumeration->ItemList;
                                     if(pData) {

                                         pData[0] = 123;
                                         pData[1] = 456;
                                         pData[2] = 789;
                                         pOutHeader->lConType  = TWON_ENUMERATION;
                                         pOutHeader->lDataSize = sizeof(TW_ENUMERATION) +
                                                       (sizeof(TW_UINT32) * 3);
                                         *pdwActualData = sizeof(TWAIN_CAPABILITY) +
                                                     sizeof(TW_ENUMERATION)   +
                                                     (sizeof(TW_UINT32) * 3);

                                         pOutHeader->lRC = TWRC_SUCCESS;
                                         pOutHeader->lCC = TWCC_SUCCESS;

                                         hr = S_OK;
                                     } else {

                              //
                              // Could not get the item list pointer.
                              //

                                         hr = E_INVALIDARG;
                                     }
                                 } // if (Enumeration)
                             } // if (pInHeader->lDataSize > 0)
                             break;
                         } // case MSG_GET

                     case MSG_SET:  // Set the incoming value.
                         {
                         // Check the TWAIN container type, and use
                         // the contained values.
                         //
                         // 1. Create a pointer to a TWAIN container
                         //    of the desired type.
                         // 2. Set the pointer of the previous step
                         //    to the address in pInHeader->Data.
                         // 3. Access the values in the TWAIN
                         //    container.
                         // 4. Carry out any private operations
                         //    with those values.
                         // 5. Set *pchActualData to the size of a
                         //    TWAIN_CAPABILITY header.
                         // 6. Set the TWAIN return codes,
                         //    pOutHeader->lRC and pOutHeader->lCC.
                         // 7. Set the HRESULT to S_OK, and return.

                             switch(pInHeader->lConType) {
                             case TWON_ONEVALUE:
                                 {
                                     pOneValue = (TW_ONEVALUE*)pInHeader->Data;
                                     if(pOneValue) {
                                         if(pOneValue->ItemType == TWTY_UINT32) {
                                             if(WriteMyPrivateTWAINValue((TW_UINT32)pOneValue->Item)) {
                                                 *pdwActualData = sizeof(TWAIN_CAPABILITY);
                                                 pOutHeader->lRC = TWRC_SUCCESS;
                                                 pOutHeader->lCC = TWCC_SUCCESS;
                                             } else {
                                                 pOutHeader->lRC = TWRC_FAILURE;
                                                 pOutHeader->lCC = TWCC_BADVALUE;
                                             }
                                             hr = S_OK;
                                         }
                                     } // if(pOneValue)
                                     break;
                                 } // case TWON_ONEVALUE:

                             default:
                                 break;
                             } // End switch(pInHeader->lConType)
                             break;
                         } // case MSG_SET
                     case MSG_RESET:   // reset TWAIN capability
                         {
                             break;
                         }
                     default:
                         {
                             // Messages other than MSG_GETCURRENT,
                             // MSG_GETDEFAULT, MSG_GET, MSG_SET
                             break;
                         }
                     } // switch(pInHeader->lMSG)
                 } // case ICAP_MY_PRIVATE1
             case ICAP_MY_PRIVATE2:
                 {
                     break;
                 }
               default:
                 {
                  // Unknown capability - set TWAIN failure codes.
                     pOutHeader->lRC = TWRC_FAILURE;
                     pOutHeader->lCC = TWCC_BADCAP;
                     break;
                 }
               } // End switch(pInHeader->lCapID)
           } // End if (pInHeader && pOutHeader)
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

 

 




