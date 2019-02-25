---
title: Bluetooth Version and Profile Support in Previous Windows Versions
description: Bluetooth Version and Profile Support in Previous Windows Versions
ms.assetid: A5A81EAA-0DC7-4725-AA0D-5C4867DDE47C
ms.date: 02/12/2018
ms.localizationpriority: medium
---

# Bluetooth Software Radio Switch Function Prototypes

> Note: Beginning with Windows 8.1 vendors are no longer required to implement radio on/off capability (for Bluetooth 4.0 radios) in a software DLL as described in this topic, because the operating system now handles this functionality. Windows 8.1 will ignore any such DLL, even if present.

For Windows 8, Bluetooth radios must support software on/off capability. To allow vendors maximal flexibility, the Bluetooth Media Radio Manager supports a plug-in to allow this functionality to be exposed to users.

To provide this DLL plug-in, two things must be done.

A DLL must be authored which exports the correct functions 
The DLL must be registered on the machine. The DLL is responsible for persisting the radio state, including across system reboots 
The DLL must export two functions:

-    BluetoothEnableRadio: The radio support DLL implements BluetoothEnableRadio to enable Windows to turn power to the radio on or off.

```cpp
C++ 
DWORD WINAPI BluetoothEnableRadio(
   BOOL fEnable
);
``` 

fEnable: Set to TRUE to turn radio power on. Set to FALSE to turn radio power off.

Return value: Return ERROR_SUCCESS if current state was changed to state of fEnable. Otherwise, returns a WIN32 error code if current state was not changed.

-    IsBluetoothRadioEnabled: The radio support DLL implements IsBluetoothRadioEnabled to enable Windows to determine if power to the radio is on or off.

```cpp
C++ 
DWORD WINAPI IsBluetoothRadioEnabled(
   BOOL* pfEnabled
);
```
pfEnabled: Pointer to buffer describing if power to the radio is on or off.

Return value: Return ERROR_SUCCESS if current state was obtained. The value pointed to by pfEnabled now contains the state. (true or false). Otherwise, returns a WIN32 error code if current state was not obtained. The value pointed to by pfEnabled is undefined and should not be used

DLL Registration

To enable the software radio switch controls in the menu and in the control panel applet, this support DLL must be registered. Set the following registry value to the full path (may include environment variables) to the DLL in question.

Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Radio Support

Value Name: “SupportDLL”

Value Data : (the path)

Example:

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Radio Support]

"SupportDLL"="C:\\Program Files\\Fabrikam\\BthSupport.dll"

It is required to install the DLL in a secure location such as C:\Program Files\Fabrikam.

Requirements and Recommendations

While this design allows flexibility in how the hardware can be controlled, it is required that the off state results in no transmission/reception from the radio. Additionally, it is recommended to power down the radio to its lowest power state to conserve energy and remove it from the bus to allow the Bluetooth stack to unload.

BluetoothEnableRadio shall only return a result after the change in radio state has occurred. Additionally, because this DLL extension is meant to provide a unified radio on/off infrastructure within Windows, usage of the DLL should be reserved for Windows components. It’s the responsibility of the DLL to ensure the correct result is returned if the DLL is also used by a non-Windows component, or if a hardware switch is implemented that could turn off the radio outside the context of the Bluetooth Media Radio Manager (e.g. a switch hardwired to power off the radio).

Windows 8 Radio Management requires the DLL to execute its instructions in the Local Service Account context. Under this context, the DLL will have the minimum privilege on the local computer, which is typically less than that of a normal user context.

The radio support DLL should perform the appropriate checks to ensure the presence of its corresponding hardware prior to performing any actions. If the corresponding hardware is not found on the system, the radio support DLL should return an appropriate error code.

## Bluetooth Software Radio Sample Sources
Registry File

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BthServ]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BthServ\Parameters]

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BthServ\Parameters\Radio Support]

"SupportDLL"=hex(2):25,00,73,00,79,00,73,00,74,00,65,00,6d,00,72,00,6f,00,6f,\

00,74,00,25,00,5c,00,73,00,79,00,73,00,74,00,65,00,6d,00,33,00,32,00,5c,00,\

72,00,73,00,75,00,70,00,70,00,6f,00,72,00,74,00,2e,00,64,00,6c,00,6c,00,00,\

00


MAKEFILE
```cpp
###### --------------------------------------------------------------------

######

###### Copyright(c) Microsoft Corp., 2012

######

###### --------------------------------------------------------------------
```

!ifdef NTMAKEENV

!INCLUDE $(NTMAKEENV)\makefile.def

!else # NTMAKEENV

!error - You forgot to set your build environment

!endif 


RSupport.cpp

/*++ Copyright (c) Microsoft Corporation. All rights reserved.

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY

KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE

IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR

PURPOSE.

Module Name:

Rsupport.cpp

Abstract:

--*/

DWORD WINAPI IsBluetoothRadioEnabled(BOOL* pfEnabled)

{

// If the radio is enabled, set *pfEnabled = TRUE else set *pfEnabled = FALSE

return ERROR_SUCCESS;

}

DWORD WINAPI BluetoothEnableRadio(BOOL fEnable)

{

if (fEnabled)

{

// Enable the radio here

}

else

{

// Disable the radio here

}

return ERROR_SUCCESS;

}


RSupport.def

/*++

Copyright (c) Microsoft Corporation. All rights reserved.

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY

KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE

IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR

PURPOSE.

Module Name:

Rsupport.def

Abstract:

--*/

LIBRARY rsupport.dll

EXPORTS

BluetoothEnableRadio

IsBluetoothRadioEnabled 


Sample SOURCES

#

# Copyright 2012 - Microsoft Corporation

#

TARGETNAME=rsupport

TARGETPATH=obj

TARGETTYPE=DYNLINK

UMTYPE=windows

USE_MSVCRT=1

TARGETLIBS= \

$(SDK_LIB_PATH)\kernel32.lib \

$(SDK_LIB_PATH)\user32.lib \

C_DEFINES=-DWIN32 -DUNICODE -D_UNICODE

SOURCES = RSupport.cpp 




