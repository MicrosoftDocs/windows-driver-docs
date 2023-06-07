---
title: INF AddComClass directive
description: An AddComClass directive is used within a com-server-install-section and registers a COM class.
ms.date: 06/05/2023
---

# INF AddComClass directive

An AddComClass is used within a com-server-install-section and registers a COM class. A COM server must define one or more classes. This section is supported for Windows 11 version `<TBD>` and later.

```inf
[com-server-install-section]

AddComClass = [com-class-name], {clsid-guid}[, flags[, com-class-install-section]]
```

## Entries

### com-class-name

Specifies the name of the COM class being installed. If this value is not passed and COM server's description is available, it will be used. This is optional and is not used by the COM runtime.

### clsid-guid

Specifies the GUID value that identifies the COM class. This can be expressed as an explicit GUID value of the form {nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn} or as a %strkey% token defined to {nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn} in a Strings section of the INF file. 

### flags

Specifies extra flags for the AddComClass directive. The flags are reserved for future use and should be left blank or set to 0

### com-class-install-section

References an INF-writer-defined section that contains information for registering the COM class. This is an optional field. For more information, see the following Remarks section, and for more information on COM classes in general, see [COM Clients and Servers](/windows/win32/com/com-clients-and-servers).

## Remarks

The system setup code registers a COM class specified by clsid-guid

Each AddComClass directive in an INF-writer-defined COM server install section can reference an INF-writer-defined com-class-install-section elsewhere in the INF file. Each INF-writer-defined section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An AddComClass directive can refer a named com-class-install-section elsewhere in the INF. Each such section has the following form:

```inf
[com-class-install-section]

[ThreadingModel = threading-model-enum]
```

### ThreadingModel

Threading model is optional and defines what threading model COM server supports.

| ThreadingModel | Description |
|---|---|
| Apartment | Single-threaded apartment |
| Both | Single-threaded or multithreaded apartment |
| Free | Multithreaded apartment |
| Neutral | Neutral apartment |

> [!NOTE]
> If threading model is not specified, the server is loaded into the first apartment that was initialized in the process.  For more information see, InProcServer32

## Example

```inf
[Device_Install.COM]
AddComServer   = VendorComServer,, VendorComServer_Inst

[VendorComServer_Inst]
ServerType     = 1 ; in-proc
ServerBinary   = %13%\Vendor_ComServer.dll
Description    = %Vendor_ComServer_Desc%
AddComClass    = VendorComClass, {bb2b85ab-9473-42e5-8d1a-0f01d3879879}
AddComClass    = VendorComClassWithThreadingModel, {f1baf99b-d28a-4ea3-b652-355da082d260}, Vendor_ComClass_WithThreadingModel_Inst

[Vendor_ComClass_WithThreadingModel_Inst]
ThreadingModel = Both

[Strings]
%Vendor_ComServer_Desc%="Vendor COM server"
```

## See also

- [Using a Component INF File](using-a-component-inf-file.md)
- [INF DDInstall.COM section](inf-ddinstall-com-section.md)
- [INF AddComServer directive](inf-addcomserver-directive.md)
- [INF AddInterface directive](inf-addinterface-directive.md)
