---
title: Using Framework Registry-Key Objects
description: Using Framework Registry-Key Objects
ms.assetid: 2236b4e1-2e17-4e59-b12e-70fff5fd7513
keywords:
- registry WDK KMDF
- registry-key objects WDK KMDF
- framework-based drivers WDK KMDF , registry
- kernel-mode drivers WDK KMDF , registry
- KMDF WDK , registry
- Kernel-Mode Driver Framework WDK , registry
- keys WDK KMDF
- opening registry keys WDK KMDF
- removing registry keys WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Framework Registry-Key Objects


Framework-based drivers access the registry by using *framework registry-key objects*. The registry-key object defines methods that enable your driver to create, open, and close registry keys; add and remove registry values; and read or write the data that is assigned to a registry value.

To open a registry key, your driver must call [**WdfRegistryOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff549919). If the key does not exist, the driver must call [**WdfRegistryCreateKey**](https://msdn.microsoft.com/library/windows/hardware/ff549917), which creates a new key and opens it.

When your driver opens a registry key, the framework creates a registry-key object that represents the opened key and returns an object handle to the driver. The driver must use the object handle to access the key, any subkeys that exist under the key, and any values that exist under the key or its subkeys.

To read the data that is currently assigned to a registry value name, the driver can call one of the following object methods:

<a href="" id="---------wdfregistryquerymemory--------"></a>[**WdfRegistryQueryMemory**](https://msdn.microsoft.com/library/windows/hardware/ff549920)  
Retrieves the data that is currently assigned to a value name, stores the data in a framework-allocated buffer, and creates a framework memory object to represent the buffer.

<a href="" id="---------wdfregistryquerymultistring--------"></a>[**WdfRegistryQueryMultiString**](https://msdn.microsoft.com/library/windows/hardware/ff549921)  
Retrieves the string data that is currently assigned to a multi-string-typed value name, creates a framework string object for each string, and adds each string object to an object collection.

<a href="" id="---------wdfregistryquerystring--------"></a>[**WdfRegistryQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff549923)  
Retrieves the string data that is currently assigned to a string-typed value name and assigns the string to a specified framework string object.

<a href="" id="---------wdfregistryqueryunicodestring--------"></a>[**WdfRegistryQueryUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff549927)  
Retrieves the string data that is currently assigned to a string-typed value name and copies the string to a specified [**UNICODE\_STRING**](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure.

<a href="" id="---------wdfregistryqueryulong--------"></a>[**WdfRegistryQueryULong**](https://msdn.microsoft.com/library/windows/hardware/ff549925)  
Retrieves the unsigned long word (REG\_DWORD) data that is currently assigned to a value name and copies the data to a specified location.

<a href="" id="---------wdfregistryqueryvalue--------"></a>[**WdfRegistryQueryValue**](https://msdn.microsoft.com/library/windows/hardware/ff549928)  
Retrieves the data that is currently assigned to a value name and copies the data to a driver-supplied buffer.

To write data to a registry value, the driver can call one of the following methods. If the value name already exists, the operating system updates the value's data.

<a href="" id="---------wdfregistryassignmemory--------"></a>[**WdfRegistryAssignMemory**](https://msdn.microsoft.com/library/windows/hardware/ff549901)  
Assigns data that is contained in a memory buffer to a specified value name in the registry.

<a href="" id="---------wdfregistryassignmultistring--------"></a>[**WdfRegistryAssignMultiString**](https://msdn.microsoft.com/library/windows/hardware/ff549903)  
Assigns a set of strings to a specified value name in the registry. The strings are contained in a driver-supplied collection of framework string objects.

<a href="" id="---------wdfregistryassignstring--------"></a>[**WdfRegistryAssignString**](https://msdn.microsoft.com/library/windows/hardware/ff549906)  
Assigns a string to a specified value name in the registry. The string is contained in a framework string object.

<a href="" id="---------wdfregistryassignunicodestring--------"></a>[**WdfRegistryAssignUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff549912)  
Assigns a specified Unicode string to a specified value name in the registry.

<a href="" id="---------wdfregistryassignulong--------"></a>[**WdfRegistryAssignULong**](https://msdn.microsoft.com/library/windows/hardware/ff549910)  
Assigns a specified unsigned long word value to a specified value name in the registry.

<a href="" id="---------wdfregistryassignvalue--------"></a>[**WdfRegistryAssignValue**](https://msdn.microsoft.com/library/windows/hardware/ff549913)  
Assigns the contents of a driver-supplied data buffer to a specified value name in the registry.

To remove a registry value, the driver must call [**WdfRegistryRemoveValue**](https://msdn.microsoft.com/library/windows/hardware/ff549932). To remove a key, the driver must call [**WdfRegistryRemoveKey**](https://msdn.microsoft.com/library/windows/hardware/ff549930).

To obtain WDM information about the registry, a driver can call [**WdfRegistryWdmGetHandle**](https://msdn.microsoft.com/library/windows/hardware/ff549935), which returns a WDM handle to the registry key that a framework registry-key object represents.

After your driver has finished accessing a registry key, it must call [**WdfRegistryClose**](https://msdn.microsoft.com/library/windows/hardware/ff549914) or [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to close the key and delete the registry-key object.

 

 





