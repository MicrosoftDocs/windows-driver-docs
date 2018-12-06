---
title: IStream Transfer Driver Example
description: IStream Transfer Driver Example
ms.assetid: fb830522-f95e-4dd7-8c1b-de092a6c5a51
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IStream Transfer Driver Example


The following code example shows an implementation of the IStream-based transfer model.

```cpp
MyWiaDriver::drvAcquireItemData(
BYTE                      *pWiasContext,
LONG                      lFlags,
PMINIDRV_TRANSFER_CONTEXT pmdtc,
LONG                      *plDevErrVal)
{
   // Check what kind of data transfer is requested.
   if (lFlags & WIA_MINIDRV_TRANSFER_DOWNLOAD)
   {
      // This transfer is a stream-based download.
      IWiaMiniDrvTransferCallback *pTransferCallback = NULL;
      hr = pmdtc->pIWiaMiniDrvCallBack->QueryInterface(IID_IWiaMiniDrvTransferCallback,
             (void**) &pIWiaMiniDrvTransferCallback);
      if (SUCCEEDED(hr))
      {
         IStream *pDestination = NULL;
         // Get the destination stream from the client.
         hr = pTransferCallback->GetNextStream(0, 
                                               bstrItemName,
                                               bstrFullItemName,
                                               &pDestination);
         if (hr == S_OK)
         {
            BYTE    *pBuffer = ...
            ULONG   ulBytesRead = 0;
            // Read the next chunk of data into the buffer.
            while(GetNextDataBand(pBuffer, &ulBytesRead))
            {
               // Write the data to the destination stream.
               // The driver does not need to know what the
               // destination is.
               hr = pDestination->Write(...);

               if (SUCCEEDED(hr))
               {
                  // Send progress
                  hr = pTransferCallback->SendMessage(...)
               }

               else
               {
                  // Take appropriate error action (for example, abort transfer)
               }

            }
         }
      }
   .
   .
   .
   }
}
```

## Related topics
[**IWiaMiniDrvTransferCallback**](https://msdn.microsoft.com/library/windows/hardware/jj151550)  



