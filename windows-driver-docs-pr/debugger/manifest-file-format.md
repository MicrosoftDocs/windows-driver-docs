---
title: Manifest File Format
description: Manifest File Format
ms.assetid: 1b0dc305-878c-4eb2-9e92-f7f7017ae4eb
keywords: ["LogViewer, manifest, file format"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Manifest File Format


## <span id="ddk_manifest_file_format_dtoolq"></span><span id="DDK_MANIFEST_FILE_FORMAT_DTOOLQ"></span>


The file format for the manifest files borrows as much from C++ and IDL as possible. As a result, it is fairly easy to take a normal C++ SDK header file and modify it to be a manifest file. The parser fully supports C and C++ style comments to help you organize and document the file.

If you are attempting to add a manifest file or make alterations to an existing file, the best way to do it is to just experiment. When you issue a **!logexts.logi** or **!logexts.loge** command in the debugger, Logger will attempt to parse the manifest files. If it encounters a problem, it will produce an error message which might indicate the mistake.

A manifest file is made up of the following basic elements: module labels, category labels, function declarations, COM interface definitions, and type definitions. Other types of elements exist as well, but these are the most important.

### <span id="module_labels"></span><span id="MODULE_LABELS"></span>Module Labels

A module label simply declares what DLL exports the functions that are declared thereafter. For example, if your manifest file is for logging a group of functions from Comctl32.dll, you would include the following module label before declaring any function prototypes:

```cpp
module COMCTL32.DLL:
```

A module label must appear before any function declarations in a manifest file. A manifest file can contain any number of module labels.

### <span id="category_labels"></span><span id="CATEGORY_LABELS"></span>Category Labels

Similar to a module label, a category label identifies which "category" all subsequent functions and/or COM interfaces belong to. For example, if you are creating a Comctl32.dll manifest file, you can use the following as your category label:

```cpp
category CommonControls:
```

A manifest file can contain any number of category labels.

### <span id="function_declarations"></span><span id="FUNCTION_DECLARATIONS"></span>Function Declarations

A function declaration is what actually prompts Logger to log something. It is nearly identical to a function prototype found in a C/C++ header file. There are a few notable additions to the format, which can be best illustrated by the following example:

```cpp
HANDLE [gle] FindFirstFileA(
       LPCSTR lpFileName,
       [out] LPWIN32_FIND_DATAA lpFindFileData);
```

The function **FindFirstFileA** takes two parameters. The first is *lpFileName*, which is a full path (usually with wildcards) defining where to search for a file or files. The second is a pointer to a WIN32\_FIND\_DATAA structure that will be used to contain the search results. The returned HANDLE is used for future calls to **FindNextFileA**. If **FindFirstFileA** returns INVALID\_HANDLE\_VALUE, then the function call failed and an error code can be procured by calling the **GetLastError** function.

The HANDLE type is declared as follows:

```cpp
value DWORD HANDLE
{
#define NULL                       0 [fail]
#define INVALID_HANDLE_VALUE      -1 [fail]
};
```

If the value returned by this function is 0 or -1 (0xFFFFFFFF), Logger will assume that the function failed, because such values have a \[fail\] modifier in the value declaration. (See the Value Types section later in this section.) Since there is a \[gle\] modifier right before the function name, Logger recognizes that this function uses **GetLastError** to return error codes, so it captures the error code and logs it to the log file.

The \[out\] modifier on the *lpFindFileData* parameter informs Logger that the data structure is filled in by the function and should be logged when the function returns.

### <span id="com_interface_definitions"></span><span id="COM_INTERFACE_DEFINITIONS"></span>COM Interface Definitions

A COM interface is basically a vector of functions that can be called by a COM object's client. The manifest format borrows heavily from the Interface Definition Language (IDL) used in COM to define interfaces.

Consider the following example:

```cpp
interface IDispatch : IUnknown
{
    HRESULT GetTypeInfoCount( UINT pctinfo  );
 
    HRESULT GetTypeInfo(
        UINT iTInfo,
        LCID lcid,
        LPVOID ppTInfo );
 
    HRESULT GetIDsOfNames(
        REFIID riid,
        LPOLECHAR* rgszNames,
        UINT cNames,
        LCID lcid,
        [out] DISPID* rgDispId );
 
    HRESULT Invoke( 
        DISPID  dispIdMember,      
        REFIID  riid,              
        LCID  lcid,                
        WORD  wFlags,              
        DISPPARAMS*  pDispParams,  
        VARIANT*  pVarResult,  
        EXCEPINFO*  pExcepInfo,  
        UINT*  puArgErr );
};
```

This declares an interface called **IDispatch** that is derived from **IUnknown**. It contains four member functions, which are declared in specific order within the interface's braces. Logger will intercept and log these member functions by replacing the function pointers in the interface's vtable (the actual binary vector of function pointers used at run time) with its own. See the COM\_INTERFACE\_PTR Types section later in this section for more details on how Logger captures interfaces as they are handed out.

### <span id="type_definitions"></span><span id="TYPE_DEFINITIONS"></span>Type Definitions

Defining data types is the most important (and most tedious) part of manifest file development. The manifest language allows you to define human-readable labels for numeric values that are passed in or returned from a function.

For example, Winerror.h defines a type called "WinError" that is a list of error values returned by most Microsoft Win32 functions and their corresponding human-readable labels. This allows Logger and LogViewer to replace uninformative error codes with meaningful text.

You can also label individual bits within a bit mask to allow Logger and LogViewer to break a DWORD bit mask into its components.

There are 13 basic types supported by the manifest. They are listed in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Type</th>
<th align="left">Length</th>
<th align="left">Display Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Pointer</p></td>
<td align="left"><p>4 bytes</p></td>
<td align="left"><p>0x001AF320</p></td>
</tr>
<tr class="even">
<td align="left"><p>VOID</p></td>
<td align="left"><p>0 bytes</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>BYTE</p></td>
<td align="left"><p>1 byte</p></td>
<td align="left"><p>0x32</p></td>
</tr>
<tr class="even">
<td align="left"><p>WORD</p></td>
<td align="left"><p>2 bytes</p></td>
<td align="left"><p>0x0A23</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DWORD</p></td>
<td align="left"><p>4 bytes</p></td>
<td align="left"><p>-234323</p></td>
</tr>
<tr class="even">
<td align="left"><p>BOOL</p></td>
<td align="left"><p>1 byte</p></td>
<td align="left"><p><strong>TRUE</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>LPSTR</p></td>
<td align="left"><p>Length byte plus any number of characters</p></td>
<td align="left"><p>&quot;Quick brown fox&quot;</p></td>
</tr>
<tr class="even">
<td align="left"><p>LPWSTR</p></td>
<td align="left"><p>Length byte plus any number of Unicode characters</p></td>
<td align="left"><p>&quot;Jumped over the lazy dog&quot;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GUID</p></td>
<td align="left"><p>16 bytes</p></td>
<td align="left"><p>{0CF774D0-F077-11D1-B1BC-00C04F86C324}</p></td>
</tr>
<tr class="even">
<td align="left"><p>COM_INTERFACE_PTR</p></td>
<td align="left"><p>4 bytes</p></td>
<td align="left"><p>0x0203404A</p></td>
</tr>
<tr class="odd">
<td align="left"><p>value</p></td>
<td align="left"><p>Dependent on base type</p></td>
<td align="left"><p>ERROR_TOO_MANY_OPEN_FILES</p></td>
</tr>
<tr class="even">
<td align="left"><p>mask</p></td>
<td align="left"><p>Dependent on base type</p></td>
<td align="left"><p>WS_MAXIMIZED | WS_ALWAYSONTOP</p></td>
</tr>
<tr class="odd">
<td align="left"><p>struct</p></td>
<td align="left"><p>Dependent on size of encapsulated types</p></td>
<td align="left"><p></p>
+ lpRect
nLeft 34
nRight 54
nTop 100
nBottom 300</td>
</tr>
</tbody>
</table>

 

Type definitions in manifest files work like C/C++ typedefs. For example, the following statement defines PLONG as a pointer to a LONG:

```cpp
typedef LONG *PLONG;
```

Most basic typedefs have already been declared in Main.h. You should only have to add typedefs that are specific to your component. Structure definitions have the same format as C/C++ struct types.

There are four special types: value, mask, GUID, and COM\_INTERFACE\_PTR.

<span id="Value_Types"></span><span id="value_types"></span><span id="VALUE_TYPES"></span>Value Types  
A value is a basic type that is broken out into human-readable labels. Most function documentation only refers to the **\#define** value of a particular constant used in a function. For example, most programmers are unaware of what the actual value is for all the codes returned by **GetLastError**, making it unhelpful to see a cryptic numerical value in LogViewer. The manifest value overcomes this by allowing value declarations like as in the following example:

```cpp
value LONG ChangeNotifyFlags
{
#define SHCNF_IDLIST      0x0000        // LPITEMIDLIST
#define SHCNF_PATHA       0x0001        // path name
#define SHCNF_PRINTERA    0x0002        // printer friendly name
#define SHCNF_DWORD       0x0003        // DWORD
#define SHCNF_PATHW       0x0005        // path name
#define SHCNF_PRINTERW    0x0006        // printer friendly name
};
```

This declares a new type called "ChangeNotifyFlags" derived from LONG. If this is used as a function parameter, the human-readable aliases will be displayed instead of the raw numbers.

<span id="Mask_Types"></span><span id="mask_types"></span><span id="MASK_TYPES"></span>Mask Types  
Similar to value types, a mask type is a basic type (usually a DWORD) that is broken out into human-readable labels for each of the bits that have meaning. Take the following example:

```cpp
mask DWORD DirectDrawOptSurfaceDescCapsFlags
{
#define DDOSDCAPS_OPTCOMPRESSED                 0x00000001
#define DDOSDCAPS_OPTREORDERED                  0x00000002
#define DDOSDCAPS_MONOLITHICMIPMAP              0x00000004
};
```

This declares a new type derived from DWORD that, if used as a function parameter, will have the individual values broken out for the user in LogViewer. So, if the value is 0x00000005, LogViewer will display:

```cpp
DDOSDCAPS_OPTCOMPRESSED | DDOSDCAPS_MONOLITHICMIPMAP
```

<span id="GUID_Types"></span><span id="guid_types"></span><span id="GUID_TYPES"></span>GUID Types  
GUIDs are 16-byte globally-unique identifiers that are used extensively in COM. They are declared in two ways:

```cpp
struct __declspec(uuid("00020400-0000-0000-C000-000000000046")) IDispatch;
```

or

```cpp
class __declspec(uuid("11219420-1768-11D1-95BE-00609797EA4F")) ShellLinkObject;
```

The first method is used to declare an interface identifier (IID). When displayed by LogViewer, "IID\_" is appended to the beginning of the display name. The second method is used to declare a class identifier (CLSID). LogViewer appends "CLSID\_" to the beginning of the display name.

If a GUID type is a parameter to a function, LogViewer will compare the value against all declared IIDs and CLSIDs. If a match is found, it will display the IID friendly name. If not, it will display the 32-hexadecimal-character value in standard GUID notation.

<span id="COM_INTERFACE_PTR_Types"></span><span id="com_interface_ptr_types"></span><span id="COM_INTERFACE_PTR_TYPES"></span>COM\_INTERFACE\_PTR Types  
The COM\_INTERFACE\_PTR type is the base type of a COM interface pointer. When you declare a COM interface, you are actually defining a new type that is derived from COM\_INTERFACE\_PTR. As such, a pointer to such a type can be a parameter to a function. If a COM\_INTERFACE\_PTR basic type is declared as an OUT parameter to a function and there is a separate parameter that has an \[iid\] label, Logger will compare the passed in IID against all declared GUIDs. If there is a match and a COM interface was declared that has the same name as the IID, Logger will hook all the functions in that interface and log them.

Here is an example:

```cpp
STDAPI CoCreateInstance(
  REFCLSID rclsid,     //Class identifier (CLSID) of the object
  LPUNKNOWN pUnkOuter, //Pointer to controlling IUnknown
  CLSCTX dwClsContext, //Context for running executable code
  [iid] REFIID riid,   //Reference to the identifier of the interface
  [out] COM_INTERFACE_PTR * ppv
                       //Address of output variable that receives 
                       //the interface pointer requested in riid
);
```

In this example, *riid* has an \[iid\] modifier. This indicates to Logger that the pointer returned in *ppv* is a COM interface pointer for the interface identified by *riid*.

It is also possible to declare a function as follows:

```cpp
DDRESULT DirectDrawCreateClipper( DWORD dwFlags, [out] LPDIRECTDRAWCLIPPER *lplpDDClipper, IUnknown *pUnkOuter );
```

In this example, LPDIRECTDRAWCLIPPER is defined as a pointer to the **IDirectDrawClipper** interface. Since Logger can identify which interface type is being returned in the *lplpDDClipper* parameter, there is no need for an \[iid\] modifier on any of the other parameters.

 

 





