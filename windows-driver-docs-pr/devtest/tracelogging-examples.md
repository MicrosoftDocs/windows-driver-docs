---
title: TraceLogging Examples
description: The source code in this topic demonstrates how to use TraceLogging.
ms.assetid: 0FD7D517-D46A-4D76-A5E1-3267DBB09A29
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TraceLogging Examples


The source code in this topic demonstrates how to use TraceLogging.

```
#include <TraceLoggingSample.h>
#include <TraceLoggingProvider.h>
#include <winmeta.h>
#include <TraceLoggingPartB_HelloWorld.h>

using namespace WEX::Common;
using namespace WEX::TestExecution;
using namespace WEX::Logging;

/*
Define a unique provider identifier
*/

/*{E98FD1FA-2218-4168-B7F8-9DE67AC89821}*/
static const GUID s_TraceLoggingSampleProviderId = { 
    0xe98fd1fa, 
    0x2218, 
    0x4168, 
    {0xb7, 0xf8, 0x9d, 0xe6, 0x7a, 0xc8, 0x98, 0x21}
};

/*
Invoke this macro to allocate storage for a provider and declare a
corresponding TraceLoggingHProvider handle variable. The provider name must be a
string literal (not a variable) and must not contain any &#39;\0&#39; characters. The
handle and copies of the handle are valid as long as the original handle is in
scope.

Note that the handle is created in the "unregistered" state and will ignore
any Write calls until it is registered.
*/
TraceLoggingProvider(g_hProvider, "TraceLoggingProviderSample");

bool TraceLoggingSample::Setup()
{
    /*
    Call this function to register your provider with ETW.
    This is analogous to the ETW EventRegister() function.
    The provider handle must be in the "unregistered" state.
    Returns ERROR_SUCCESS if the provider was successfully registered.
    Note that it is ok to ignore failure - if TraceLoggingRegisterByGuid
    fails, TraceLoggingWrite and TraceLoggingUnregister will be no-ops.
    */
    ULONG RegisterResult = TraceLoggingRegisterByGuid(g_hProvider, 
        &s_TraceLoggingSampleProviderId);
    
    VERIFY_WIN32_SUCCEEDED(RegisterResult, L"Failed to register TraceLogging");


    return true;
}

bool TraceLoggingSample::Cleanup()
{
    /*
    Call this function to unregister your provider.  Once unregistered,
    TraceLoggingWrite will be a no-op until the provider is registered again.
    Analogous to the ETW EventUnregister() function.
    */
    TraceLoggingUnregister(g_hProvider);


    return true;
}

void TraceLoggingSample::BasicDataTypes()
{
    UINT8 u8 = 200;
    INT32 i32 = -2000000000;
    UINT32 u32 = 4000000000;
    INT64 i64 = 9000000000000000000;
    float f32 = 3.14f;
    BOOL b = TRUE;
    bool bcpp = true;

    /*
    The following four "NumericValues" events are equivalent (except where noted) ...
    */

    TraceLoggingWrite(
        g_hProvider,
        "NumericValues",
        TraceLoggingUInt8(u8, "UINT8"),”
        TraceLoggingInt32(i32, "INT32"),
        TraceLoggingUInt32(u32, "UINT32"),
        TraceLoggingHexUInt32(u32, "UINT32"),
        TraceLoggingInt64(i64, "INT64"),
        TraceLoggingFloat32(f32, "float"),
        TraceLoggingBool(b, "BOOL"),
        TraceLoggingBool(bcpp, "bool (C++)") 
        );

    /*
    same as ...
    */

    TraceLoggingWrite(
        g_hProvider,
        "NumericValues",
        TraceLoggingUInt8(200, "UINT8"),
        TraceLoggingInt32(-2000000000, "INT32"),
        TraceLoggingUInt32(4000000000, "UINT32"),
        TraceLoggingHexUInt32(4000000000, "UINT32"),
        TraceLoggingInt64(9000000000000000000, "INT64"),
        TraceLoggingFloat32(3.14f, "float"),
        TraceLoggingBool(TRUE, "BOOL"),
        TraceLoggingBool(true, "bool (C++)")  
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
        "NumericValues",
        TraceLoggingValue(u8, "UINT8"),
        TraceLoggingValue(i32, "INT32"),
        TraceLoggingValue(u32, "UINT32"),
        TraceLoggingValue(u32, "UINT32"),
        TraceLoggingValue(i64, "INT64"),
        TraceLoggingValue(f32, "float"),
        TraceLoggingValue(b, "BOOL"),         // This will be evaluated as INT32, not as BOOL
        TraceLoggingValue(bcpp, "bool (C++)") // This will be evaluated as UINT8, not as bool
        );

    TraceLoggingWrite(
        g_hProvider,
        "NumericValues",
        TraceLoggingValue((BYTE)200, "UINT8"),
        TraceLoggingValue(-2000000000, "INT32"),
        TraceLoggingValue(4000000000, "UINT32"),
        TraceLoggingValue(4000000000, "UINT32"),    // This one won&#39;t show up as hex. 
                                                    // TraceLoggingValue will use default out types
        TraceLoggingValue(9000000000000000000, "INT64"),
        TraceLoggingValue(3.14f, "float"),
        TraceLoggingValue((BOOL)TRUE, "BOOL"),      // This will be evaluated as INT32, not as BOOL
        TraceLoggingValue((bool)true, "bool (C++)") // This will be evaluated as UINT8, not as bool
        );

#endif


    /*
    Strings and chars
    */

    TraceLoggingWrite(
        g_hProvider,
        "Strings and Chars",
        TraceLoggingString("She loves me ...", "String (char)"), 
        TraceLoggingWideString(L"She loves me not ...", "String (wide char)"), 
        TraceLoggingChar(&#39;A&#39;, "Single char"),
        TraceLoggingWchar(L&#39;z&#39;, "Single wide char")
        );


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

    GetSystemTime(&st);
    GetSystemTimeAsFileTime(&ft);

    TraceLoggingWrite(
        g_hProvider,
        "Other Types",
        TraceLoggingGuid(s_TraceLoggingSampleProviderId, "GUID"), 
        TraceLoggingFileTime(ft, "Current Time (SYSTEMTIME)"), 
        TraceLoggingSystemTime(st, "Current Time (FILETIME)"), 
        TraceLoggingSid(sid1, "SID"),  
        TraceLoggingPointer((LPCVOID)this, "void*"),
        TraceLoggingIntPtr(iptr, "INT_PTR"),
        TraceLoggingUIntPtr(uptr, "UINT_PTR")
        );
}

void TraceLoggingSample::NamingData()
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
        TraceLoggingUInt32(Cat) 
        );

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingValue(Cat)  
        );


    /*
    Let&#39;s use a different symbol for the value of the event&#39;s "Cat" field.  
    */
    
    UINT32 Tiger = Cat;
    
    /*
    Now we need to explicitly name the datum or we will have events with a 
    different field name ("Tiger").
    */

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingUInt32(Tiger, "Cat")
        );

    TraceLoggingWrite(
        g_hProvider,
        "MoreThanOneWayToSkinACat",
        TraceLoggingValue(Tiger, "Cat")
        );
};

void TraceLoggingSample::LevelsAndKeywords()
{
    /*
    Verbosity levels and event keywords must be compile-time constants.

    TraceLoggingLevel accepts values 0-255
    TraceLoggingKeyword accepts values 0 to UINT64_MAX

    See winmeta.h for predefined verbosity levels and reserved keyword values.
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
        TraceLoggingValue(Status, "Current Status")
        );

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_BLUE | MY_PROVIDER_KEYWORD_YELLOW),
        TraceLoggingValue(Status, "Current Status")
        );

    TraceLoggingWrite(
        g_hProvider,
        "Keywords",
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_BLUE),
        TraceLoggingKeyword(MY_PROVIDER_KEYWORD_YELLOW),
        TraceLoggingValue(Status, "Current Status")
        );
}

void TraceLoggingSample::Arrays()
{
    INT32 IntValsFixed[5] = {20, 21, 22, 23, 24};
    UINT cIntVals = 5;
    INT32* IntValsVar = new INT32[cIntVals];

    VERIFY_IS_NOT_NULL(IntValsVar);
    memcpy(IntValsVar, IntValsFixed, sizeof(IntValsFixed));


    /*
    Variable size arrays
    */

    TraceLoggingWrite(
        g_hProvider,
        "Variable Size Arrays",
        TraceLoggingInt32Array(IntValsVar, (UINT16)cIntVals, "Variable size int array"), 
        TraceLoggingInt32Array(IntValsVar, 5, "Variable size int array")  
        );


    /*
    Fixed size arrays

    Fixed size array macros use the "FixedArray" suffix.
    The absence of the suffix indicates a variable sized array.
    */

    TraceLoggingWrite(
        g_hProvider,
        "Constant Size Arrays", 
        TraceLoggingInt32FixedArray(IntValsFixed, _countof(IntValsFixed), 
            "Constant size int array")      
        );

    delete [] IntValsVar;
}

void TraceLoggingSample::Structs()
{
    WIN32_FIND_DATA FindData;
    HANDLE hFind = FindFirstFile(L".", &FindData);

    VERIFY_IS_TRUE(hFind != INVALID_HANDLE_VALUE);

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
    ... or ...
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

void TraceLoggingSample::PartB()
{
    SYSTEMTIME st;
    GetSystemTime(&st);

    TraceLoggingWrite(
        g_hProvider,
        "ExampleWithPartB",
        TraceLoggingValue(st, "Part C: Current Time"),
        TraceLoggingPartB_Ms_HelloWorld(
            "Bond, James",              // Alias
            "TraceLoggingExamples",     // Tutorial Name
            8,                          // Rating (1-10) 
            "Ready to instrument"),     // Feedback      
        TraceLoggingValue("Happy tracing!", "Part C: Closing Message")
        );
}
```

 

 





