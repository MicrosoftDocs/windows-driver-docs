---
title: Time Travel Debugging - Sample App Walkthrough
description: This section contains a walk through of a small C++ app. 
ms.author: windowsdriverdev
ms.date: 09/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small logo on windbg preview](images/windbgx-preview-logo.png) Time Travel Debugging - Sample App Walkthrough

This section  a walk through of a small C++ app.

TBD TBD TBD

## Sample Code

Compile this code using Visual Studio.

```
// CDog_Console.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <windows.h>
class CDog
{
public:
       CDog() { m_age = 8; m_weight = 30; }
       long m_age;
       long m_weight;
};

class CDogs
{
public:
       CDog MyDog1;
       CDog MyDog2;
       CDog MyDog3;
       CDog MyDog4;
       CDog MyDog5;

};

class Simple1DArray
{
public:
       ULONG64 m_size =5;
       int intArray[5]{ 1,2,3,4,5 };
       int *m_pValues = &intArray[0];
       Simple1DArray()
       {
       };

};



int main()
{
       CDog MyDog;
       CDogs MyDogs;
       Simple1DArray g_array1D;
       printf_s("Array Information \n");
       printf_s("%I64d, %d \n", g_array1D.m_size, (int) g_array1D.m_pValues);
       printf_s("Array size Dog Object Information \n");
       printf_s("%d, %d\n", MyDog.m_age, MyDog.m_weight);
       getchar();
       return 0;
}
```

## Recording the App

TBD

## Playing back the App

TBD


> Additional Content Pending

---

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20Using%20WinDbg%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




