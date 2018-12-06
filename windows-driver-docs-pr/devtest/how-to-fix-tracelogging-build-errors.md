---
title: How to fix TraceLogging build errors
description: This topic describes some common build errors and how to resolve them.
ms.assetid: E0C7ACA5-68C9-40FF-8D6E-4A65CEB0A851
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to fix TraceLogging build errors


This topic describes some common build errors and how to resolve them.

## <span id="Case_1___DECLSPEC_SAFEBUFFERS__errors"></span><span id="case_1___declspec_safebuffers__errors"></span><span id="CASE_1___DECLSPEC_SAFEBUFFERS__ERRORS"></span>Case 1: 'DECLSPEC\_SAFEBUFFERS' errors


<span id="Build_Error__snippet__"></span><span id="build_error__snippet__"></span><span id="BUILD_ERROR__SNIPPET__"></span>Build Error (snippet):  
```
1>traceloggingprovider.h(1592): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;TLG_STATUS&#39;
1>traceloggingprovider.h(1592): error C2433: &#39;DECLSPEC_SAFEBUFFERS&#39; : &#39;inline&#39; not permitted on data declarations
1>traceloggingprovider.h(1592): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
```

<span id="Fix_"></span><span id="fix_"></span><span id="FIX_"></span>Fix:  
Include windows.h before including TraceLoggingProvider.h in your source file.

## <span id="Case_2__TraceLogging_in_Modern_C___Apps"></span><span id="case_2__tracelogging_in_modern_c___apps"></span><span id="CASE_2__TRACELOGGING_IN_MODERN_C___APPS"></span>Case 2: TraceLogging in Modern C++ Apps


<span id="Build_Error__snippet__"></span><span id="build_error__snippet__"></span><span id="BUILD_ERROR__SNIPPET__"></span>Build Error (snippet):  
After copying the TraceLogging header files into your build environment and adding this line:

```
TraceLoggingRegisterByGuid(g_3DBuilderTraceProvider, &s_3DBuilderTraceProviderGuid);
```

You got this linker error:

```
Error 2 error LNK2001: unresolved external symbol __imp__EventSetInformation@20 
        E:\TFS\Main\PrintPreviewR5\Viewers\PrintPreview\App.xaml.obj    PrintPreview
Error 3 error LNK2001: unresolved external symbol __imp__EventRegister@16       
        E:\TFS\Main\PrintPreviewR5\Viewers\PrintPreview\App.xaml.obj    PrintPreview
```

<span id="Fix_"></span><span id="fix_"></span><span id="FIX_"></span>Fix:  
UWP apps need to link against advapi32.lib to resolve this reference issue.

## <span id="Case_3__Phone_Builds"></span><span id="case_3__phone_builds"></span><span id="CASE_3__PHONE_BUILDS"></span>Case 3: Phone Builds


<span id="Build_Error__snippet__"></span><span id="build_error__snippet__"></span><span id="BUILD_ERROR__SNIPPET__"></span>Build Error (snippet):  
When compiling the file dictationuimodel.cpp, you get the error:

```
traceloggingprovider.h(1592) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;TLG_STATUS&#39;
traceloggingprovider.h(1592) : error C2433: &#39;DECLSPEC_SAFEBUFFERS&#39; : &#39;inline&#39; not permitted on data declarations
```

<span id="Fix_"></span><span id="fix_"></span><span id="FIX_"></span>Fix:  
See Case\#1. It is likely that your SDK does not define the macro **DECLSPEC\_SAFEBUFFERS**. Up-to-date SDKs have a definition for this macro. If your SDK does not define this macro, you will need to provide your own definition. **DECLSPEC\_SAFEBUFFERS** is defined in winnt.h, which should be included by windows.h. Also, until the public release of the Windows 10 SDK you may need to define the *Telemetry* keyword:

```
#ifndef WINEVENT_KEYWORD_TELEMETRY 
#define WINEVENT_KEYWORD_TELEMETRY  0x2000000000000
#endif
```

 

 





