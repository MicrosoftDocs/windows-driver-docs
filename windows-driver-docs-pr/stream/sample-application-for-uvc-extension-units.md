---
title: Sample Application for UVC Extension Units
description: This topic contains sample application code that you can use to support Extension Units.
keywords:
- extension units WDK USB Video Class , samples, sample application
- sample code WDK USB Video Class , UVC extension units
ms.date: 09/17/2021
---

# Sample application for UVC extension units

> [!IMPORTANT]
> The content and sample code in this topic is outdated and currently unsupported. It may not work with the current driver development toolchain.

This topic contains sample application code that you can use to support Extension Units.

An application accesses the interface by using [**IKsTopologyInfo::CreateNodeInstance**](/previous-versions/ms785846(v=vs.85)) followed by a call to **QueryInterface** on the node object to obtain the required COM API. For more information, see [**IKsTopologyInfo**](/previous-versions/ms785854(v=vs.85)).

Include the following code in the application source, arbitrarily named TestApp.cpp.

Also include in TestApp.cpp the code shown in [Supporting Autoupdate Events with Extension Units](supporting-autoupdate-events-with-extension-units.md).

```cpp
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
