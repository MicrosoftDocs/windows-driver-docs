---
title: Verify Framework
description: Verify Framework
ms.assetid: A954B5E2-E3C7-4021-BE53-AE1257139607
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verify Framework


To make writing Tests easier, TAEF provides the "Verify" framework that takes advantage of the [WexLogger](wexlogger.md) to report detailed logs with a minimal amount of code. The Verify framework helps Tests to provide structured log output - it outputs a successful log if a given verification succeeds, and it outputs detailed information if a verification fails.

## <span id="cplusplus"></span><span id="CPLUSPLUS"></span>Using Verify From C++


The Verify API is surfaced in C++ as a set of macros that are defined in the "Verify.h" header file (Note: You do not need to explicitly include Verify.h, you should include "WexTestClass.h" which contains everything you need for marking-up C++ tests and interacting with the Verify and WexLogger API's).

The following Verify Macros are available for Native C++ Tests:

| Macro                                                                                     | Functionality                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VERIFY\_ARE\_EQUAL(expected, actual, \[optional message\])                                | Verifies that two specified objects are equal. Also logs a custom message if provided.                                                                                                                                |
| VERIFY\_ARE\_NOT\_EQUAL(expected, actual, \[optional message\])                           | Verifies that two specified objects are not equal. Also logs a custom message if provided.                                                                                                                            |
| VERIFY\_IS\_GREATER\_THAN(expectedGreater, expectedLess, \[optional message\])            | Verifies that the first parameter is greater than the second parameter. Also logs a custom message if provided.                                                                                                       |
| VERIFY\_IS\_GREATER\_THAN\_OR\_EQUAL(expectedGreater, expectedLess, \[optional message\]) | Verifies that the first parameter is greater than or equal to the second parameter. Also logs a custom message if provided.                                                                                           |
| VERIFY\_IS\_LESS\_THAN(expectedLess, expectedGreater, \[optional message\])               | Verifies that the first parameter is less than the second parameter. Also logs a custom message if provided.                                                                                                          |
| VERIFY\_IS\_LESS\_THAN\_OR\_EQUAL(expectedLess, expectedGreater, \[optional message\])    | Verifies that the first parameter is less than or equal to the second parameter. Also logs a custom message if provided.                                                                                              |
| VERIFY\_ARE\_SAME(expected, actual, \[optional message\])                                 | Verifies that the two parameters specified refer to the same object. Also logs a custom message if provided.                                                                                                          |
| VERIFY\_ARE\_NOT\_SAME(expected, actual, \[optional message\])                            | Verifies that the two parameters specified do not refer to the same object. Also logs a custom message if provided.                                                                                                   |
| VERIFY\_FAIL (\[optional message\])                                                       | Fails without checking any conditions. Also logs a custom message if provided.                                                                                                                                        |
| VERIFY\_IS\_TRUE(condition, \[optional message\])                                         | Verifies that the specified bool is true. Call VERIFY\_IS\_TRUE(!!\_\_condition), or VERIFY\_WIN32\_BOOL\_SUCCEEDED(\_\_condition) to test a Win32 BOOL. Also logs a custom message if provided.                      |
| VERIFY\_IS\_FALSE(condition, \[optional message\])                                        | Verifies that the specified bool is false. Call VERIFY\_IS\_FALSE(!!\_\_condition), or VERIFY\_WIN32\_BOOL\_FAILED(\_\_condition) to test a Win32 BOOL. Also logs a custom message if provided.                       |
| VERIFY\_IS\_NULL(object, \[optional message\])                                            | Verifies that the specified parameter is NULL. Also logs a custom message if provided.                                                                                                                                |
| VERIFY\_IS\_NOT\_NULL(object, \[optional message\])                                       | Verifies that the specified parameter is not NULL. Also logs a custom message if provided.                                                                                                                            |
| VERIFY\_SUCCEEDED(hresult, \[optional message\])                                          | Verifies that the specified HRESULT is successful. Also logs a custom message if provided.                                                                                                                            |
| VERIFY\_SUCCEEDED\_RETURN(hresult, \[optional message\])                                  | Verifies that the specified HRESULT is successful and returns the HRESULT that was passed into the macro. Also logs a custom message if provided.                                                                     |
| VERIFY\_FAILED(hresult, \[optional message\])                                             | Verifies that the specified HRESULT is not successful. Also logs a custom message if provided.                                                                                                                        |
| VERIFY\_FAILED\_RETURN(hresult, \[optional message\])                                     | Verifies that the specified HRESULT is not successful and returns the HRESULT that was passed into the macro. Also logs a custom message if provided.                                                                 |
| VERIFY\_THROWS(operation, exception, \[optional message\])                                | Verifies that the specified operation throws the given exception type. Also logs a custom message if provided.                                                                                                        |
| VERIFY\_NO\_THROW(operation, \[optional message\])                                        | Verifies that the specified operation does not throw an exception. Also logs a custom message if provided.                                                                                                            |
| VERIFY\_WIN32\_SUCCEEDED(win32Result, \[optional message\])                               | Verifies that the specified Win32 result succeeded. Also logs a custom message if provided.                                                                                                                           |
| VERIFY\_WIN32\_SUCCEEDED\_RETURN(win32Result, \[optional message\])                       | Verifies that the specified Win32 result succeeded and returns the LONG that was passed into the macro. Also logs a custom message if provided.                                                                       |
| VERIFY\_WIN32\_FAILED(win32Result, \[optional message\])                                  | Verifies that the specified Win32 result failed. Also logs a custom message if provided.                                                                                                                              |
| VERIFY\_WIN32\_FAILED\_RETURN(win32Result, \[optional message\])                          | Verifies that the specified Win32 result failed and returns the LONG that was passed into the macro. Also logs a custom message if provided.                                                                          |
| VERIFY\_WIN32\_BOOL\_SUCCEEDED(win32Bool, \[optional message\])                           | Verifies that the specified Win32 BOOL succeeded (!= FALSE). Will log the result of GetLastError() if verification fails. Also logs a custom message if provided.                                                     |
| VERIFY\_WIN32\_BOOL\_SUCCEEDED\_RETURN(win32Bool, \[optional message\])                   | Verifies that the specified Win32 BOOL succeeded (!= FALSE) and returns the BOOL that was passed into the macro. Will log the result of GetLastError() if verification fails. Also logs a custom message if provided. |
| VERIFY\_WIN32\_BOOL\_FAILED(win32Bool, \[optional message\])                              | Verifies that the specified Win32 BOOL failed (== FALSE). Does not log the result of GetLastError(). Also logs a custom message if provided.                                                                          |
| VERIFY\_WIN32\_BOOL\_FAILED\_RETURN(win32Bool, \[optional message\])                      | Verifies that the specified Win32 BOOL failed (== FALSE) and returns the BOOL that was passed into the macro. Does not log the result of GetLastError(). Also logs a custom message if provided.                      |



### <span id="exception_cplusplus"></span><span id="EXCEPTION_CPLUSPLUS"></span>Exception Based Verify Usage

If your source code is compiled with C++ exceptions enabled (by specifying the "/EHsc" command line switch, or the "USE\_NATIVE\_EH=1" macro in a sources file), then the Verify macros will default to logging an error on failure, followed by throwing a native C++ exception. The exception thrown is a **WEX::TestExecution::VerifyFailureException**. You do not need to catch this exception - the TAEF framework will catch it for you and move on to the next test case.

Optionally, if you would like to perform a series of verifications in a row rather than having the test abort on the first verification failure, you can use the **DisableVerifyExceptions** class. The object's lifetime controls the amount of time that exceptions are disabled.

```cpp
if (NULL != m_key)
{
    DisableVerifyExceptions disable;
    VERIFY_WIN32_SUCCEEDED(::RegDeleteKey(HKEY_CURRENT_USER, zTempName));
    VERIFY_WIN32_SUCCEEDED(::RegCloseKey(m_key));
}
```

In the example above, exceptions are disabled only within the "if (NULL != m\_key)" block, and if the first verify call fails, the second verify call is still made.

The **DisableVerifyExceptions** class is ref-counted, and also functions on a per-thread basis.

### <span id="nonexception_cplusplus"></span><span id="NONEXCEPTION_CPLUSPLUS"></span>Non-Exception Based Verify Usage

If your source code is ***not*** compiled with C++ exceptions enabled, the Verify macros will not throw a native C++ when verifications fail. Additionally, if your source code is compiled with C++ exceptions enabled but you want to disable Verify exceptions, simply \#define NO\_VERIFY\_EXCEPTIONS before including "WexTestClass.h".

In this model, you must perform a series of nested if statements in order to control the flow of your test case, rather than relying on C++ exceptions.

```cpp
if (VERIFY_WIN32_SUCCEEDED(::RegDeleteKey(HKEY_CURRENT_USER, zTempName)))
{
    ...
}
```

### <span id="outsettings_cplusplus"></span><span id="OUTSETTINGS_CPLUSPLUS"></span>Verify Output Settings

If you would like to customize the output produced by the Verify APIs, you can use the **SetVerifyOutput** class. The object's lifetime controls the amount of time that the output settings are set. The **SetVerifyOutput** class is ref-counted, and functions on a per-thread basis.

```cpp
if (NULL != m_key)
{
    SetVerifyOutput verifySettings(VerifyOutputSettings::LogOnlyFailures);
    VERIFY_IS_TRUE(true, L"Should NOT log a comment");
    VERIFY_IS_TRUE(false, L"Should log an error");
}
VERIFY_IS_TRUE(true, L"Should log a comment");
```

In the example above, the specified settings only pertain to calls made within the "if (NULL != m\_key)" block, and *only* the verify call that fails will be logged. However, the third verify call will be logged even though it succeeds. This is due to the fact that the SetVerifyOutput class has gone out of scope.

The following options exist for setting the verify output:

<span id="VerifyOutputSettings__LogOnlyFailures_"></span><span id="verifyoutputsettings__logonlyfailures_"></span><span id="VERIFYOUTPUTSETTINGS__LOGONLYFAILURES_"></span>VerifyOutputSettings::LogOnlyFailures   
Only failed verify calls will be logged; all successful calls are ignored.

<span id="VerifyOutputSettings__LogFailuresAsBlocked_"></span><span id="verifyoutputsettings__logfailuresasblocked_"></span><span id="VERIFYOUTPUTSETTINGS__LOGFAILURESASBLOCKED_"></span>VerifyOutputSettings::LogFailuresAsBlocked   
Log all failures as blocked rather than logging an error.

<span id="VerifyOutputSettings__LogFailuresAsWarnings_"></span><span id="verifyoutputsettings__logfailuresaswarnings_"></span><span id="VERIFYOUTPUTSETTINGS__LOGFAILURESASWARNINGS_"></span>VerifyOutputSettings::LogFailuresAsWarnings   
Log all failures as warnings rather than logging an error.

<span id="VerifyOutputSettings__LogValuesOnSuccess_"></span><span id="verifyoutputsettings__logvaluesonsuccess_"></span><span id="VERIFYOUTPUTSETTINGS__LOGVALUESONSUCCESS_"></span>VerifyOutputSettings::LogValuesOnSuccess   
Log the values of parameters passed in, even when the Verify call succeeds.

Verify output settings can be OR'd together to enable multiple settings:

```cpp
SetVerifyOutput verifySettings(VerifyOutputSettings::LogOnlyFailures | VerifyOutputSettings::LogFailuresAsBlocked);
```

### <span id="outcustom_cplusplus"></span><span id="OUTCUSTOM_CPLUSPLUS"></span>Providing Value Output for Custom Types

The C++ Verify framework provides the ability to generate detailed output for any custom type. In order to do so, one must implement a specialization of the **WEX::TestExecution::VerifyOutputTraits** class template.

The **WEX::TestExecution::VerifyOutputTraits** class template specialization must exist in the **WEX::TestExecution** namespace. It is also expected to provide a public static method called **ToString**, which takes a reference to your class, and returns a **WEX::Common::NoThrowString** containing a string representation of its value.

```cpp
    class MyClass
    {
    public:
        MyClass(int value)
            : m_myValue(value)
        {
        }

        int GetValue()
        {
            return m_myValue;
        }

    private:
        int m_myValue;
    }

    namespace WEX { namespace TestExecution
    {
        template <>
        class VerifyOutputTraits<MyClass>
        {
        public:
            static WEX::Common::NoThrowString ToString(const MyClass& myClass)
            {
                return WEX::Common::NoThrowString().Format(L"%d", myClass.GetValue());
            }
        };
    }}
```

### <span id="comparators_cplusplus"></span><span id="COMPARATORS_CPLUSPLUS"></span>Providing Comparators for Custom Types

The C++ Verify framework provides the ability to define comparators for custom types that do not implement corresponding operator overloads (operator=, operator&lt;, etc). In order to do so, one must implement a specialization of the **WEX::TestExecution::VerifyCompareTraits** class template.

The **WEX::TestExecution::VerifyCompareTraits** class template specialization must exist in the **WEX::TestExecution** namespace. It is also expected to provide a public static methods called **AreEqual**, **AreSame**, **IsLessThan**, **IsGreaterThan**, and **IsNull**.

```cpp
    class MyClass
    {
    public:
        MyClass(int value)
            : m_myValue(value)
        {
        }

        int GetValue()
        {
            return m_myValue;
        }

    private:
        int m_myValue;
    }

    namespace WEX { namespace TestExecution
    {
        template <>
        class VerifyCompareTraits<MyClass, MyClass>
        {
        public:
            static bool AreEqual(const MyClass& expected, const MyClass& actual)
            {
                return expected.GetValue() == actual.GetValue();
            }

            static bool AreSame(const MyClass& expected, const MyClass& actual)
            {
                return &expected == &actual;
            }

            static bool IsLessThan(const MyClass& expectedLess, const MyClass& expectedGreater)
            {
                return (expectedLess.GetValue() < expectedGreater.GetValue());
            }

            static bool IsGreaterThan(const MyClass& expectedGreater, const MyClass& expectedLess)
            {
                return (expectedGreater.GetValue() > expectedLess.GetValue());
            }

            static bool IsNull(const MyClass& object)
            {
                return object.GetValue() == 0;
            }
        };
    }}
```

## <span id="csharp"></span><span id="CSHARP"></span>Using Verify From C#


The C# Verify usage is similar to that of C++. However, it is provided via the **WEX.TestExecution.Verify** class, which is located within **Te.Managed.dll**.

The following Verify methods are available for C# tests:

| Macro                                                                                       | Functionality                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AreEqual(object expected, object actual)                                                    | Verifies that two specified objects are equal.                                                                                                                                      |
| AreEqual(object expected, object actual, string message)                                    | Verifies that two specified objects are equal; logs a custom message on verification success or failure.                                                                            |
| AreEqual&lt;T&gt;(T expected, T actual)                                                     | Verifies that two specified objects are equal.                                                                                                                                      |
| AreEqual&lt;T&gt;(T expected, T actual, string message)                                     | Verifies that two specified objects are equal; logs a custom message on verification success or failure.                                                                            |
| AreNotEqual(object expected, object actual)                                                 | Verifies that two specified objects are not equal.                                                                                                                                  |
| AreNotEqual(object expected, object actual, string message)                                 | Verifies that two specified objects are not equal; logs a custom message on verification success or failure.                                                                        |
| AreNotEqual&lt;T&gt;(T expected, T actual)                                                  | Verifies that two specified objects are not equal.                                                                                                                                  |
| AreNotEqual&lt;T&gt;(T expected, T actual, string message)                                  | Verifies that two specified objects are not equal; logs a custom message on verification success or failure.                                                                        |
| AreSame(object expected, object actual)                                                     | Verifies that the two parameters specified refer to the same object.                                                                                                                |
| AreSame(object expected, object actual, string message)                                     | Verifies that the two parameters specified refer to the same object; logs a custom message on verification success or failure.                                                      |
| AreNotSame(object expected, object actual)                                                  | Verifies that the two parameters specified do not refer to the same object.                                                                                                         |
| AreNotSame(object expected, object actual, string message)                                  | Verifies that the two parameters specified do not refer to the same object; logs a custom message on verification success or failure.                                               |
| IsGreaterThan(IComparable expectedGreater, IComparable expectedLess)                        | Verifies that the first parameter is greater than the second parameter.                                                                                                             |
| IsGreaterThan(IComparable expectedGreater, IComparable expectedLess, string message)        | Verifies that the first parameter is greater than the second parameter; logs a custom message on verification success or failure.                                                   |
| IsGreaterThanOrEqual(IComparable expectedGreater, IComparable expectedLess)                 | Verifies that the first parameter is greater than or equal to the second parameter.                                                                                                 |
| IsGreaterThanOrEqual(IComparable expectedGreater, IComparable expectedLess, string message) | Verifies that the first parameter is greater than or equal to the second parameter; logs a custom message on verification success or failure.                                       |
| IsLessThan(IComparable expectedLess, IComparable expectedGreater)                           | Verifies that the first parameter is less than the second parameter.                                                                                                                |
| IsLessThan(IComparable expectedLess, IComparable expectedGreater, string message)           | Verifies that the first parameter is less than the second parameter; logs a custom message on verification success or failure.                                                      |
| IsLessThanOrEqual(IComparable expectedLess, IComparable expectedGreater)                    | Verifies that the first parameter is less than or equal to the second parameter.                                                                                                    |
| IsLessThanOrEqual(IComparable expectedLess, IComparable expectedGreater, string message)    | Verifies that the first parameter is less than or equal to the second parameter; logs a custom message on verification success or failure.                                          |
| Fail(string message)                                                                        | Fails without checking any conditions.                                                                                                                                              |
| IsTrue(bool condition)                                                                      | Verifies that the specified condition is true.                                                                                                                                      |
| IsTrue(bool condition, string message)                                                      | Verifies that the specified condition is true; logs a custom message on verification success or failure.                                                                            |
| IsFalse(bool condition)                                                                     | Verifies that the specified condition is false.                                                                                                                                     |
| IsFalse(bool condition, string message)                                                     | Verifies that the specified condition is false; logs a custom message on verification success or failure.                                                                           |
| IsNull(object obj)                                                                          | Verifies that the specified parameter is NULL.                                                                                                                                      |
| IsNull(object obj, string message)                                                          | Verifies that the specified parameter is NULL; logs a custom message on verification success or failure.                                                                            |
| IsNotNull(object obj)                                                                       | Verifies that the specified parameter is not NULL.                                                                                                                                  |
| IsNotNull(object obj, string message)                                                       | Verifies that the specified parameter is not NULL; logs a custom message on verification success or failure.                                                                        |
| Throws&lt;T&gt;(VerifyOperation operation)                                                  | Verifies that the specified operation throws the given exception type. Also returns the exception for further inspection.                                                           |
| Throws&lt;T&gt;(VerifyOperation operation, string message)                                  | Verifies that the specified operation throws the given exception type; logs a custom message on verification success or failure. Also returns the exception for further inspection. |
| NoThrow(VerifyOperation operation)                                                          | Verifies that the specified operation does not throw an exception.                                                                                                                  |
| NoThrow(VerifyOperation operation, string message)                                          | Verifies that the specified operation does not throw an exception; logs a custom message on verification success or failure.                                                        |



### <span id="exception_csharp"></span><span id="EXCEPTION_CSHARP"></span>Exception Based Verify Usage

When Verification failures occur in C# test cases, an error is written to the logger, and a **WEX.TestExecution.VerifyFailureException** is thrown. Just as in the native C++ model, you do not need to worry about catching these exceptions. The TAEF framework will catch it for you and move on to the next test case.

Optionally, if you would like to perform a series of verifications in a row rather than having the test abort on the first verification failure, you can use the **DisableVerifyExceptions** class. The object's lifetime controls the amount of time that exceptions are disabled. The **DisableVerifyExceptions** class is ref-counted, and functions on a per-thread basis.

```cpp
using (new DisableVerifyExceptions())
{
    Verify.AreSame(item1, item2);
    Verify.AreEqual(item1, item2);
}
```

In the example above, if the first verify call fails, the second verify call is still made.

Alternatively, you can achieve the same result by setting **Verify.DisableVerifyExceptions = true** before the Verify operations such as the example shown below.

```cpp
Verify.DisableVerifyExceptions = true;
try
{
    Verify.AreSame(item1, item2);
    Verify.AreEqual(item1, item2);
}
finally
{
    Verify.DisableVerifyExceptions = false;
}
```

Note that even though such option is available, declaring DisableVerifyExeptions as an object in a using block is still the recommended option.

If you want to stop in the debugger when a verification error occurs bring up the exceptions dialog (Ctrl+Alt+E), click Add, choose "Common Language Runtime Exceptions" in the dropdown and put "WEX.TestExecution.VerifyFailureException" in the Name field.

### <span id="outsettings_csharp"></span><span id="OUTSETTINGS_CSHARP"></span>Verify Output Settings

If you would like to customize the output produced by the Verify APIs, you can use the **SetVerifyOutput** class. The object's lifetime controls the amount of time that the output settings are set. The **SetVerifyOutput** class is ref-counted, and functions on a per-thread basis.

```cpp
using (new SetVerifyOutput(VerifyOutputSettings.LogOnlyFailures))
{
    Log.Comment("Only the following error should be logged:");
    Verify.IsTrue(true, "Should NOT log a comment");
    Verify.IsTrue(false, "Should log an error");
}
Verify.IsTrue(true, "Should log a comment");
```

In the example above, only the second verify call should be logged since it's the only call that fails within the using block. However, the third verify call *will* be logged even though it succeeds. This is due to the fact that the SetVerifyOutput class has gone out of scope.

Alternatively, you can achieve the same result by setting **Verify.OutputSettings = VerifyOutputSettings.LogOnlyFailures** before the Verify operations such as the example shown below.

```cpp
Verify.OutputSettings = VerifyOutputSettings.LogFailuresAsWarnings
try
{
    Verify.AreSame(item1, item2);
    Verify.AreEqual(item1, item2);
}
finally
{
    Verify.OutputSettings = VerifyOutputSettings.None;
}
```

Note that even though such option is available, declaring SetVerifyOutput as an object in a using block is still the recommended option.

The following options exist for setting the verify output:

<span id="verifyoutputsettings.logonlyfailures_"></span><span id="VERIFYOUTPUTSETTINGS.LOGONLYFAILURES_"></span>VerifyOutputSettings.LogOnlyFailures   
Only failed verify calls will be logged; all successful calls are ignored.

<span id="verifyoutputsettings.logfailuresasblocked_"></span><span id="VERIFYOUTPUTSETTINGS.LOGFAILURESASBLOCKED_"></span>VerifyOutputSettings.LogFailuresAsBlocked   
Log all failures as blocked rather than logging an error.

<span id="verifyoutputsettings.logfailuresaswarnings_"></span><span id="VERIFYOUTPUTSETTINGS.LOGFAILURESASWARNINGS_"></span>VerifyOutputSettings.LogFailuresAsWarnings   
Log all failures as warnings rather than logging an error.

Verify output settings can be OR'd together to enable multiple settings:

```cpp
using (new SetVerifyOutput(VerifyOutputSettings.LogFailuresAsBlocked | VerifyOutputSettings.LogOnlyFailures))
{
...
}
```

## <span id="script"></span><span id="SCRIPT"></span>Using Verify From Script


The Verify API is also surfaced for script languages, following the same usage patterns as C++ and C#.

### <span id="Installation"></span><span id="installation"></span><span id="INSTALLATION"></span>Installation

When using the scriptable verify API's from within a TAEF test method no installation is necessary - the required API's are registered using 'Registration Free COM'. In order to use the scriptable API from outside a TAEF test method (outside TAEF, or in a child-process) simply register the Te.Common.dll binary using regsvr32 from an elevated command prompt; for example:

``` syntax
regsvr32 Te.Common.dll
```

When deploying TAEF using a deployment file for lab execution, Te.Common.dll is automatically registered.

### <span id="usage_script"></span><span id="USAGE_SCRIPT"></span>Usage

The scriptable Verify API's are surfaced through the 'TE.Common.Verify' COM class - simply instantiate that class and call methods on it - the Verify class will automatically work with WEXLogger to write pass and fail verifications to the log.

```cpp
1   <?xml version="1.0" ?>
2   <?component error="false" debug="false"?>
3   <package>
4     <component id="Example">
5       <object id="Log" progid="Wex.Logger.Log" />
6       <object id="Verify" progid="Te.Common.Verify" />
7       <reference guid="e65ef678-a232-42a7-8a36-63108d719f31" version="1.0"/>
8       <reference guid="f8bb9db9-e54e-4555-b3e5-e3ddf2fef401" version="1.0"/>
9
10      <public>
11        <method name="HelloWorld"/>
12      </public>
13
14      <script language="JScript">
15          function HelloWorld() {
16              Verify.IsTrue(true);
17              Verify.IsFalse(false);
18          }
19      </script>
20    </component>
21  </package>
```

This example defines a TAEF script test class with a single 'HelloWorld' method. Line 6 uses the 'object' element to define the Verify variable in the global scope. Line 8 uses the 'reference' element to include all constants from the specified type-library (in this case, Te.Common.dll's type library) into the global scope of the script; in this case it adds the 'VerifySettings' constants. Lines 16 and 17 show simply usage of the Verify API's. When executed, the example will generate the following output:

``` syntax
Test Authoring and Execution Framework v2.7 Build 6.2.7922.0 (fbl_esc_end_dev(mschofie).110202-1000) For x86

StartGroup: Example::HelloWorld
Verify: IsTrue
Verify: IsFalse
EndGroup: Example::HelloWorld [Passed]

Summary: Total=1, Passed=1, Failed=0, Blocked=0, Not Run=0, Skipped=0
```

### <span id="api_script"></span><span id="API_SCRIPT"></span>Scriptable Verify API

The methods for validation on the scriptable Verify API are as follows:

| Method                                                                                | Functionality                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bool Verify.AreEqual(expected, actual, \[optional message\])                          | Verifies that the two values are equal. If the 'VerifySettings\_CoerceTypes' setting is enabled, this method uses the JScript definition of equality, if the 'VerifySettings\_CoerceTypes' setting is not enabled, the method uses the JScript definition of identity. **'VerifySettings\_CoerceTypes' is on by default.**     |
| bool Verify.AreNotEqual(expected, actual, \[optional message\])                       | Verifies that the two values not are equal. If the 'VerifySettings\_CoerceTypes' setting is enabled, this method uses the JScript definition of equality, if the 'VerifySettings\_CoerceTypes' setting is not enabled, the method uses the JScript definition of identity. **'VerifySettings\_CoerceTypes' is on by default.** |
| bool Verify.IsGreaterThan(expectedGreater, expectedLess, \[optional message\])        | Verifies that the first value is greater than the second.                                                                                                                                                                                                                                                                      |
| bool Verify.IsGreaterThanOrEqual(expectedGreater, expectedLess, \[optional message\]) | Verifies that the first value is greater than or equal to the second.                                                                                                                                                                                                                                                          |
| bool Verify.IsLessThan(expectedLess, expectedGreater, \[optional message\])           | Verifies that the first value is less than the second.                                                                                                                                                                                                                                                                         |
| bool Verify.IsLessThanOrEqual(expectedLess, expectedGreater, \[optional message\])    | Verifies that the first value is less than or equal to the second.                                                                                                                                                                                                                                                             |
| bool Verify.AreSame(expected, actual, \[optional message\])                           | Verifies that the values are the same.                                                                                                                                                                                                                                                                                         |
| bool Verify.AreNotSame(expected, actual, \[optional message\])                        | Verifies that the values are not the same.                                                                                                                                                                                                                                                                                     |
| bool Verify.Fail(\[optional message\])                                                | Fails without checking conditions.                                                                                                                                                                                                                                                                                             |
| bool Verify.IsTrue(expression, \[optional message\])                                  | Verifies that the given expression evaluates to true.                                                                                                                                                                                                                                                                          |
| bool Verify.IsFalse(expression, \[optional message\])                                 | Verifies that the given expression evaluates to false.                                                                                                                                                                                                                                                                         |
| bool Verify.IsNull(expected, \[optional message\])                                    | Verifies that the given value is 'null'.                                                                                                                                                                                                                                                                                       |
| bool Verify.IsNotNull(expected, \[optional message\])                                 | Verifies that the given value is not 'null'.                                                                                                                                                                                                                                                                                   |
| bool Verify.Throws(function, \[optional message\])                                    | Verifies that the given function throws and exception.                                                                                                                                                                                                                                                                         |
| bool Verify.NoThrow(function, \[optional message\])                                   | Verifies that the given function does not throw and exception.                                                                                                                                                                                                                                                                 |



There are two methods on the Verify class for controlling the settings:

| Method                                  | Functionality                                         |
|-----------------------------------------|-------------------------------------------------------|
| object Verify.EnableSettings(settings)  | The specified setting flag or flags will be enabled.  |
| object Verify.DisableSettings(settings) | The specified setting flag or flags will be disabled. |



The settings value passed to the Verify.EnableSettings or Verify.DisableSettings methods can be any of the following values:

<span id="VerifySettings_LogOnlyFailures___0x01"></span><span id="verifysettings_logonlyfailures___0x01"></span><span id="VERIFYSETTINGS_LOGONLYFAILURES___0X01"></span>VerifySettings\_LogOnlyFailures = 0x01  
Only failures are logged - there is no output on successful Verify calls.

<span id="VerifySettings_LogFailuresAsBlocked___0x02"></span><span id="verifysettings_logfailuresasblocked___0x02"></span><span id="VERIFYSETTINGS_LOGFAILURESASBLOCKED___0X02"></span>VerifySettings\_LogFailuresAsBlocked = 0x02  
Failures are logged as 'Blocked', instead of the default 'Error'.

<span id="VerifySettings_LogFailuresAsWarnings___0x04"></span><span id="verifysettings_logfailuresaswarnings___0x04"></span><span id="VERIFYSETTINGS_LOGFAILURESASWARNINGS___0X04"></span>VerifySettings\_LogFailuresAsWarnings = 0x04  
Failures are logged as 'Warning', instead of the default 'Error'.

<span id="VerifySettings_LogValuesOnSuccess___0x08"></span><span id="verifysettings_logvaluesonsuccess___0x08"></span><span id="VERIFYSETTINGS_LOGVALUESONSUCCESS___0X08"></span>VerifySettings\_LogValuesOnSuccess = 0x08  
The values of parameters to verify are written as part of the Verify log message. **This is on by default.**

<span id="VerifySettings_CoerceTypes___0x1000"></span><span id="verifysettings_coercetypes___0x1000"></span><span id="VERIFYSETTINGS_COERCETYPES___0X1000"></span>VerifySettings\_CoerceTypes = 0x1000  
The values passed to the Verify methods will be coerced following the JScript coercion rules. **This is on by default.**

<span id="VerifySettings_DisableExceptions___0x2000"></span><span id="verifysettings_disableexceptions___0x2000"></span><span id="VERIFYSETTINGS_DISABLEEXCEPTIONS___0X2000"></span>VerifySettings\_DisableExceptions = 0x2000  
Exceptions will not be thrown when a validation fails.

### <span id="settings_script"></span><span id="SETTINGS_SCRIPT"></span>Verify Settings

The Verify API provides settings to configure it's behavior. The 'EnableSettings' and 'DisableSettings' methods can be used to enable or disable specific settings that the Verify class maintains. The methods take one or more settings to enable or disable.

```cpp
    Verify.EnableSettings(VerifySettings_LogOnlyFailures);
```

To enable or disable multiple settings in one call, you can include multiple 'VerifySettings' flags:

```cpp
    Verify.EnableSettings(VerifySettings_LogOnlyFailures | VerifySettings_DisableExceptions);
```

The EnableSettings and DisableSettings methods return an object that can be used to restore the original settings, allowing settings to be enabled or disabled for a given scope;

```cpp
1    var guard = Verify.EnableSettings(VerifySettings_LogOnlyFailures);
2    try
3    {
4        Verify.AreEqual(10, 0xa);
5    }
6    finally
7    {
8        guard.Restore();
9    }
```

In this example, the Verify.EnableSettings method is passed 'VerifySettings\_LogOnlyFailures', which will be incorporated with the settings that are already present on the Verify object. A Verify call is made within a try-finally block, so that during the finally block, the 'guard' object can be used to restore the original settings.

### <span id="exception_script"></span><span id="EXCEPTION_SCRIPT"></span>Exception Based Verify Usage

By default the Verify methods will throw an exception when a verification fails. When running under TAEF if the exception is thrown out of the test method, the test will be failed. For example:

```cpp
1    var guard = Verify.EnableSettings(VerifySettings_CoerceTypes);
2    try
3    {
4        Verify.AreEqual(1, "1");
5        Verify.AreEqual("1", 1);
6    }
7    finally
8    {
9        guard.Restore();
10   }
```

In this example, the second Verify call will never be made, since the first will throw an exception and fail the test. The settings support on the Verify API can be used to change this behavior, so that failed verifications do not throw, which would allow subsequent Verify calls to be made. This is particularly useful to Verify a set of parameters, and make sure that all verifications are written out.

```cpp
1    var guard = Verify.EnableSettings(VerifySettings_CoerceTypes | VerifySettings_DisableExceptions);
2    try
3    {
4        Verify.AreEqual(1, "1");
5        Verify.AreEqual("1", 1);
6    }
7    finally
8    {
9        guard.Restore();
10   }
```

Because exceptions were disabled, both verifications will be written to the log.

### <span id="outsideapi_script"></span><span id="OUTSIDEAPI_SCRIPT"></span>Using the Scriptable Verify API Outside TAEF

The scriptable Verify API can be used outside TAEF. Make sure that the Te.Common.dll is registered, as called out in the [Installation section](#installation), and simple create the "TE.Common.Verify" class.

```cpp
var VerifySettings_DisableExceptions = 0x2000;

var Verify = new ActiveXObject("TE.Common.Verify");
var Log = new ActiveXObject("WEX.Logger.Log");

Verify.EnableSettings(VerifySettings_DisableExceptions);

Log.StartGroup("Group A");
Verify.AreEqual(1, 2);
Log.EndGroup("Group A");

Log.StartGroup("Group B");
Verify.AreEqual(2, 2);
Log.EndGroup("Group B");
```

The preceding code will generate the follow console output when executed through cscript:

``` syntax
StartGroup: Group A
Error: Verify: AreEqual - Values (1, 2)
EndGroup: Group A [Failed]

StartGroup: Group B
Verify: AreEqual - Values (2, 2)
EndGroup: Group B [Passed]

Non-passing Tests:

    Group A [Failed]

Summary: Total=2, Passed=1, Failed=1, Blocked=0, Not Run=0, Skipped=0
```

The ['WEX.Logger.Log' API](wexlogger.md) can be used to configure the WEX Logger as needed (for example, as a child process), and the scriptable Verify API will take advantage of that configuration.









