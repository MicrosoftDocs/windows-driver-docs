---
title: Runtime Parameters
description: Runtime Parameters
ms.assetid: 5CE5D2C3-F967-4318-B799-38CE8E8B15A6
---

# Runtime Parameters


TAEF provides functionality for passing runtime parameters to the tests it executes.

## <span id="Usage"></span><span id="usage"></span><span id="USAGE"></span>Usage


To pass a parameter to your test, supply this parameter to te.exe as a command line parameter in the following form:

``` syntax
Te.exe /p:ParameterName1=ParameterValue1  /p:ParameterName2=ParameterValue2
```

If the parameter value contains spaces, put quotes around parameter name and parameter value:

``` syntax
Te.exe /p:"ParameterName3=The quick brown fox jumps over the lazy dog"
```

## <span id="Built-in_Parameters"></span><span id="built-in_parameters"></span><span id="BUILT-IN_PARAMETERS"></span>Built-in Parameters


TAEF has built-in support for the following Runtime Parameters:

-   TestDeploymentDir: The test binary directory.
-   TestName: The name of the test which is currently running.
-   FullTestName: The full name of the test including variation qualifiers. This is the name as TAEF logs it for StartGroup and EndGroup.
-   TestResult: The aggregate worst-case result of tests executed within the scope of this Cleanup function. In order from best to worst: Passed, NotRun, Skipped, Blocked, Failed. For example, if at least one test in your class was blocked but no tests failed, the result will be "Blocked" (only available in Cleanup functions).

## <span id="Accessing_Runtime_Parameters_from_Tests"></span><span id="accessing_runtime_parameters_from_tests"></span><span id="ACCESSING_RUNTIME_PARAMETERS_FROM_TESTS"></span>Accessing Runtime Parameters from Tests


### <span id="Native_Tests"></span><span id="native_tests"></span><span id="NATIVE_TESTS"></span>Native Tests

Runtime Parameters are available in Setup, Cleanup and test methods. Use the RuntimeParameters::TryGetValue API to obtain them:

```
String value;
VERIFY_SUCCEEDED(RuntimeParameters::TryGetValue(L"ParameterName3", value));
```

Note: In order to request Runtime Parameters from your tests, you will need to link against Te.Common.lib library.

### <span id="Managed_Tests"></span><span id="managed_tests"></span><span id="MANAGED_TESTS"></span>Managed Tests

Runtime Parameters are available in setup and test methods. To obtain them, use the TestContext property of your class.

Example (class or assembly setup):

```
[ClassInitialize]

public static void ClassSetup(TestContext context)
{
    String parameterName3  = context.Properties["ParameterName3"];

}
```

Similarly, from a test:

```
[TestMethod]

public void VerifyRuntimeParametersTest()
{
    String parameterName3  = m_testContext.Properties["ParameterName3"].ToString());
}

// Note, that to work with runtime parameters, as well as with your tests,  you need to add
// definition of test context property to your class

private TestContext m_testContext;

public TestContext TestContext
{
    get { return m_testContext; }
    set { m_testContext = value; }
}
```

### <span id="Script_Tests"></span><span id="script_tests"></span><span id="SCRIPT_TESTS"></span>Script Tests

Runtime parameters are available in the setup, cleanup and the test methods. To retrieve runtime parameters, define and instantiate the RuntimeParameters object from Te.Common:

```
<object id="RuntimeParameters" progid="Te.Common.RuntimeParameters" />
```

Once the RuntimeParameters object is instantiated, you can use RuntimeParameters.Contains("&lt;runtime parameter name&gt;") method to query if a runtime parameter was supplied and is available to the test. If it returns true, you can then use RuntimeParameters.GetValue("&lt;runtime parameter name&gt;") to retrieve it. Note that RuntimeParameters.GetValue(...) will throw if the runtime parameter is not available. The following example is from our VBScript example:

```
       <script language="VBScript">
            <![CDATA[
                Function TestOne()
                    dim param
                    param = "No runtime param"
                    If RuntimeParameters.Contains("param") Then
                         param = RuntimeParameters.GetValue("param")
                    End If
                    Log.Comment("Param is " + param)

                    dim testDir
                    If RuntimeParameters.Contains("testDir") Then
                        testDir = RuntimeParameters.GetValue("TestDir")
                    End If
                    Log.Comment("The test harness is running in " + testDir)
                End Function
            ]] >
        </script>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Runtime%20Parameters%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




