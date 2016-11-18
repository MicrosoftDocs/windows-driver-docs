---
title: Sample Application for UVC Extension Units
author: windows-driver-content
description: Sample Application for UVC Extension Units
MS-HAID:
- 'uvcds\_4f4db094-13e5-4915-9525-14a381ec9221.xml'
- 'stream.sample\_application\_for\_uvc\_extension\_units'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f900b0b1-3469-442f-8593-2094a0966d4a
keywords: ["extension units WDK USB Video Class , samples, sample application", "sample code WDK USB Video Class , UVC extension units"]
---

# Sample Application for UVC Extension Units


This topic contains sample application code that you can use to support Extension Units.

An application accesses the interface by using **IKsTopologyInfo::CreateNodeInstance** followed by a call to **QueryInterface** on the node object to obtain the required COM API. The **IKsTopologyInfo** interface is documented on the [MSDN Library](http://go.microsoft.com/fwlink/p/?linkid=27252) website.

Include the following code in the application source, arbitrarily named TestApp.cpp.

Also include in TestApp.cpp the code shown in [Supporting Autoupdate Events with Extension Units](supporting-autoupdate-events-with-extension-units.md).

```
  // pUnkOuter is the unknown associated with the base filter
  hr = pUnkOuter->QueryInterface(__uuidof(IKsTopologyInfo), 
                               (void **) &pKsTopologyInfo);
  if (!SUCCEEDED(hr))
  {
        printf("Unable to obtain IKsTopologyInfo %x\n", hr);
 goto errExit;
  }

  hr = FindExtensionNode(pKsTopologyInfo,                                                                                                   
     GUID_EXTENSION_UNIT_DESCRIPTOR,
     &dwExtensionNode);
  if (FAILED(hr))
  {
        printf("Unable to find extension node : %x\n", hr);
 goto errExit;
  }

  hr = pKsTopologyInfo->CreateNodeInstance(
        dwExtensionNode, 
   __uuidof(IExtensionUnit), 
 (void **) &pExtensionUnit);
 if (FAILED(hr))
  {
        printf("Unable to create extension node instance : %x\n", hr);
 goto errExit;
  }

  hr = pExtensionUnit->get_PropertySize(1, &ulSize);
  if (FAILED(hr))
  {
        printf("Unable to find property size : %x\n", hr);
 goto errExit;
  }

  pbPropertyValue = new BYTE[ulSize];
  if (!pbPropertyValue)
  {
      printf("Unable to allocate memory for property value\n");
      goto errExit;
  }

  hr = pExtensionUnit->get_Property(1,ulSize, pbPropertyValue);
  if (FAILED(hr))
  {
      printf("Unable to get property value\n");
      goto errExit;
  }
 
  // assume the property value is an integer
  ASSERT(ulSize == 4);
  printf("The value of property 1 = %d\n", *((int *) 
     pbPropertyValue));
```

In this case, **pUnkOuter** should be a pointer to the capture filter that represents the USB Video Class (UVC) device. After you add the capture filter to the filter graph, you can query the filter for the **IKsTopologyInfo** interface as shown in this sample code.

Write the code for the **FindExtensionNode** function to locate the necessary extension unit node and to return its ID in *dwExtensionNode*. This ID is used in this sample code's subsequent call to the **IKsTopologyInfo::CreateNodeInstance** method.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Sample%20Application%20for%20UVC%20Extension%20Units%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


