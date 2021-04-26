---
title: TraceLogging Examples
description: The source code in this topic demonstrates how to use TraceLogging.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceLogging Examples


The source code in this topic demonstrates how to use TraceLogging.

```
#include <windows.h>
#include <TraceLoggingProvider.h>
#include <winmeta.h>

/*
Invoke this macro to allocate storage for a provider and declare a
corresponding handle symbol. The provider name must be a string literal (not a
variable) and must not contain any '\0' characters.

Note that the handle is created in the "unregistered" state and will ignore
any TraceLoggingWrite calls until it is registered.
*/
TRACELOGGING_DEFINE_PROVIDER(
    g_hProvider,
    "TraceLoggingProviderSample",
    // {a12b3f0b-1161-5d99-1553-a9194ee77d81}
    (0xa12b3f0b, 0x1161, 0x5d99, 0x15, 0x53, 0xa9, 0x19, 0x4e, 0xe7, 0x7d, 0x81));

ULONG StartUp()
{
    /*
    Call this function to register your provider with ETW.
    This is analogous to the ETW EventRegister() function.
    The provider handle must be in the "unregistered" state.
    Returns ERROR_SUCCESS if the provider was successfully registered.
    Note that it is ok to ignore failure - if TraceLoggingRegister
    fails, TraceLoggingWrite and TraceLoggingUnregister will be no-ops.
    */
    ULONG RegisterResult = TraceLoggingRegister(g_hProvider);
    
    return RegisterResult;
}

ULONG ShutDown()
{
    /*
    Call this function to unregister your provider.  Once unregistered,
    TraceLoggingWrite will be a no-op until the provider is registered again.
    Analogous to the ETW EventUnregister() function.
    */
    TraceLoggingUnregister(g_hProvider);


    return ERROR_SUCCESS;
}

void BasicDataTypes()
{
    UINT8 u8 = 200;
    INT32 i32 = -2000000000;
    UINT32 u32 = 4000000000;
    INT64 i64 = 9000000000000000000;
    float f32 = 3.14f;
    BOOL b = TRUE;
    BOOLEAN bcpp = TRUE;

    /*
    The following four "NumericValues" events are equivalent (except where noted) ...
    */

    TraceLoggingWrite(
        g_hProvider,
        "NumericValues",
        TraceLoggingUInt8(u8, "MyUINT8_field"),
        TraceLoggingInt32(i32, "MyINT32_field"),
        TraceLoggingUInt32(u32, "MyUINT32_field"),
        TraceLoggingHexUInt32(u32, "MyHexUINT32_field"),
        TraceLoggingInt64(i64, "MyINT64_field"),
        TraceLoggingFloat32(f32, "My_float_field"),
        TraceLoggingBool(b, "MyBool32_field"),
        TraceLoggingBoolean(bcpp, "MyBool8_field") 
        );

    /*
    same as ...
    */

#ifdef __cplusplus

    /*
    TraceLoggingValue() automatically determines the value type (C++ only)
    */

    TraceLoggingWrite(
        g_hProvider,
        "NumericValuesCpp",
        TraceLoggingValue(u8,  "MyUINT8"),
        TraceLoggingValue(i32, "MyINT32"),
        TraceLoggingValue(u32, "MyUINT32"),
        TraceLoggingValue(i64, "MyINT64"),
        TraceLoggingValue(f32, "MyFloat"),
        TraceLoggingValue(b,   "MyBOOL32"), // Since BOOL is a typedef for int, this will be evaluated as TraceLoggingInt32, not as TraceLoggingBool
        TraceLoggingValue(bcpp, "MyBool8"));

#endif


    /*
    Strings and chars
    */

    TraceLoggingWrite(
        g_hProvider,
        "Strings and Chars",
        TraceLoggingString("She loves me ...", "String (char)"), 
        TraceLoggingWideString(L"She loves me not ...", "String (wide char)"), 
        TraceLoggingChar('A', "Single char"),
        TraceLoggingWChar(L'z', "Single wide char"));

    /*
    Other types
    */

    /*
    NOTE:
    In C, a GUID, FILETIME, or SYSTEMTIME value parameter must be an l-value.
    */

    INT_PTR iptr = 1234;
    UINT_PTR uptr = 4321;
    FILETIME ft;
    SYSTEMTIME st;
    SID const sid1 = { SID_REVISION, 1, 5, { 6 } };
    GUID g = {0};

    GetSystemTime(&st);
    GetSystemTimeAsFileTime(&ft);

    TraceLoggingWrite(
        g_hProvider,
        "Other Types",
        TraceLoggingGuid(g, "GUID"), 
        TraceLoggingFileTime(ft, "Current Time (FILETIME)"), 
        TraceLoggingSystemTime(st, "Current Time (SYSTEMTIME)"), 
        TraceLoggingSid(&sid1, "SID"),  
        TraceLoggingPointer((LPCVOID)&g, "void*"),
        TraceLoggingIntPtr(iptr, "INT_PTR"),
        TraceLoggingUIntPtr(uptr, "UINT_PTR")
        );
}

void NamingData()
{
    UINT32 Cat = 0xCA7;

    /*
    Each of the following four events are equivalent:
    */

    /*
    TraceLogging uses the symbol to automatically name the field "Cat"
    and assign it the value contained in the variable Cat (0xCA7).
    */

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingUInt32(Cat, "Cat")  // Field explicitly named "Cat"
        );

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingUInt32(Cat) // Field automatically named "Cat" named based on the expression Cat.
        );

    /*
    Let's use a different symbol for the value of the event's "Cat" field.  
    */
    
    UINT32 Tiger = Cat;
    
    /*
    Now we need to explicitly name the datum or we will have events with a 
    different field name ("Tiger").
    */

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingUInt32(Tiger, "Cat") // Field explicitly named "Cat"
        );

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingUInt32(Tiger) // Field automatically named "Tiger".
        );
};

void LevelsAndKeywords()
{
    /*
    Verbosity levels and event keywords must be compile-time constants.

    TraceLoggingLevel accepts values 0..255, though only 0..5 are well-defined.
    0 means "always". 1 means "fatal". 2 means "error". 3 means "warning".
    4 means "info". 5 means "verbose". If TraceLoggingLevel is not set for an
    event, the default is 5 (verbose).

    See winmeta.h for predefined verbosity levels.

    TraceLoggingKeyword is a 64-bit bitfield. The top 16 bits are reserved by
    Microsoft for special situations. The low 48 bits are available for
    definition on a per-provider basis.
    */

    PCWSTR MyName = L"Joe";
    INT16 MyRank = 99;
    ULONG MySerialNumber = 12345;

    /*
    The following is only logged when session verbosity level is 
    WINEVENT_LEVEL_VERBOSE (5) or higher ...  
    */

    TraceLoggingWrite(
        g_hProvider,
        "Levels",
        TraceLoggingLevel(WINEVENT_LEVEL_VERBOSE),
        TraceLoggingWideString(MyName, "Name"),
        TraceLoggingInt16(MyRank, "Rank"),
        TraceLoggingUInt32(MySerialNumber, "Serial Number")
        );

    /*
    TraceLoggingWrite will not complain if TraceLoggingLevel is invoked more than once.  
    However, only the last level will be used.  
    The following event is only logged at WINEVENT_LEVEL_VERBOSE or higher...
    */

    TraceLoggingWrite(
        g_hProvider,
        "Levels",
        TraceLoggingLevel(WINEVENT_LEVEL_CRITICAL),
        TraceLoggingLevel(WINEVENT_LEVEL_VERBOSE),
        TraceLoggingWideString(MyName, "Name"),
        TraceLoggingInt16(MyRank, "Rank"),
        TraceLoggingUInt32(MySerialNumber, "Serial Number")
        );

    /*
    Keywords, however, can be combined using multiple TraceLoggingKeyword() macros ...
    */

#define MY_PROVIDER_KEYWORD_BLUE    0x1
#define MY_PROVIDER_KEYWORD_YELLOW  0x2
#define MY_PROVIDER_KEYWORD_GREEN   (MY_PROVIDER_KEYWORD_BLUE | MY_PROVIDER_KEYWORD_YELLOW) 

    PCWSTR Status = L"Feeling a bit green";

    /*
    These events are equivalent ...
    */

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_GREEN),
        TraceLoggingWideString(Status, "Current Status")
        );

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_BLUE | MY_PROVIDER_KEYWORD_YELLOW),
        TraceLoggingWideString(Status, "Current Status")
        );

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_BLUE),
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_YELLOW),
        TraceLoggingWideString(Status, "Current Status")
        );
}

void Arrays()
{
    INT32 IntVals[5] = {20, 21, 22, 23, 24};
    UINT cIntVals = 5;

    /*
    Variable size arrays
    */

    TraceLoggingWrite(
        g_hProvider,
        "Variable Size Arrays",
        TraceLoggingInt32Array(IntVals, (UINT16)cIntVals, "Variable size int array")
        );

    /*
    Fixed size arrays

    Fixed size array macros use the "FixedArray" suffix.
    The absence of the suffix indicates a variable sized array.
    */

    TraceLoggingWrite(
        g_hProvider,
        "Constant Size Arrays", 
        TraceLoggingInt32FixedArray(IntVals, _countof(IntVals),
            "Constant size int array"));
}

void Structs()
{
    WIN32_FIND_DATA FindData;
    HANDLE hFind = FindFirstFile(L".", &FindData);
    if (hFind == INVALID_HANDLE_VALUE)
    {
        return;
    }

    /*
    TraceLoggingStruct defines a group of related fields in an event.
    The first parameter, which must be a compile-time constant, indicates
    the number of subsequent fields that are to be considered part of the 
    struct.
    */

    TraceLoggingWrite(
        g_hProvider,
        "FindFirstFile",
        TraceLoggingStruct(5, "FileData"),                           
            TraceLoggingWideString(FindData.cFileName, "Name"),   
            TraceLoggingUInt32(FindData.dwFileAttributes, "Attributes"),              
            TraceLoggingFileTime(FindData.ftCreationTime, "CreateTime"),              
            TraceLoggingUInt32(FindData.nFileSizeHigh, "SizeHigh"),              
            TraceLoggingUInt32(FindData.nFileSizeLow, "SizeLow"),
        TraceLoggingPointer(hFind, "Result")
        );

    /*
    If you commonly use the same set of fields, you might define a helper macro.
    */

#define LogWin32FindData(fd) \
    TraceLoggingStruct(5, "FileData"), \
    TraceLoggingWideString(((fd).cFileName), "Name"), \
    TraceLoggingUInt32(((fd).dwFileAttributes), "Attributes"), \
    TraceLoggingFileTime(((fd).ftCreationTime), "CreateTime"), \
    TraceLoggingUInt32(((fd).nFileSizeHigh), "SizeHigh"), \
    TraceLoggingUInt32(((fd).nFileSizeLow), "SizeLow")

    TraceLoggingWrite(
        g_hProvider,
        "FindFirstFile",
        LogWin32FindData(FindData),
        TraceLoggingPointer(hFind, "Result")
        );

    FindClose(hFind);
}

int __cdecl
main()
{
    // Note:
    StartUp();
    BasicDataTypes();
    NamingData();
    LevelsAndKeywords();
    Arrays();
    Structs();
    ShutDown();
}
```
