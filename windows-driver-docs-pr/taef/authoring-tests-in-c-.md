---
title: Authoring Tests in C#
description: Authoring Tests in C#
ms.assetid: 4DD1D673-FEAF-44a4-8BAD-0E55318DC64B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authoring Tests in C#


The example below shows a C# .cs file with a simple single test class that demostrates C# tests markup. (Please note that this example is for demonstrational purpose only, so it will not compile or run.)

```cpp
1    using Microsoft.VisualStudio.TestTools.UnitTesting;
2    using System;
3    using System.Collections;
4    using WEX.Logging.Interop;
5    using WEX.TestExecution;
6
7    [TestClass]
8    public class ManagedStartMenuTests
9    {
10       [AssemblyInitialize]
11       [TestProperty("Component", "Navigation")]
12       [TestProperty("SubComponent", "StartMenu")]
13       public static void RunModuleSetup(Object context)
14       {
15           defaultPolicy = SetObjectFactoryPolicy(PolicyClassic);
16       }
17
18       [AssemblyCleanup]
19       public static void RunModuleCleanup()
20       {
21           SetObjectFactoryPolicy(defaultPolicy);
22       }
23
24       [ClassInitialize]
25       [TestProperty("TeamOwner", "WEX")]
26       [TestProperty("GroupOwner", "MediaPlayerTest")]
27       public static void TestClassSetup(Object testContext)
28       {
29           objectFactory = new ObjectFactory();
30       }
31
32       [ClassCleanup]
33       public static void TestClassCleanup()
34       {
35           objectFactory.Dispose();
36       }
37
38       [TestInitialize]
39       public void TestMethodSetup()
40       {
41           startMenuObject = objectFactory.CreateObject();
42       }
43
44       [TestCleanup]
45       public void TestMethodCleanup()
46       {
47           startMenuObject.Dispose();
48       }
49
50
51       [TestMethod]
52       [Owner("Someone")]
53       [Priority(0)]
54       public void TestMethod1()
55       {
56           Verify.AreEqual(startMenuObject.size, expectedObjectSize);
57       }
58   }
```

For declaring c\# tests, TAEF uses VSTS test markup.

To declare a test class in C#, you use \[TestClass\] attribute on an ordinary C# class (Line 7) and for a test method declaration, use \[TestMethod\] attribute on an ordinary class method (Line 51).

C# test markup also supports full range of setup and cleanup methods.

Static method with \[AssemblyInitialize\] attribute set runs before any other class methods and performs assembly level initialization (Line 10) . Consequently, there is an assembly cleanup method, a static method with \[AssemblyCleanup\] attribute set that runs after all other methods complete (Line 18).

Similarly, there exist class and test setup and cleanup methods. (see lines 24, 32, 38, 44) Unlike in C++, class setup and cleanup methods in managed code must be static.

TAEF C# test markup supports test, class, and module properties.

To set module properties, set attributes on an assembly initializer (see lines 11 and 12). Similarly to set class level properties, set properties on a class initializer (see lines 25 and 26). For a test method level property, just apply the property to a particular test method. (see lines 52 and 53)

## <span id="Running_under_VSTS"></span><span id="running_under_vsts"></span><span id="RUNNING_UNDER_VSTS"></span>Running under VSTS


Note: to reduce the dependency on VSTS binaries, currently Class and Assembly setup methods take Object as a first parameter.

If you'd like to run the tests from VSTS, please change that Object type to **TestContext** type. Keep in mind that this will add a dependency on *microsoft.visualstudio.qualitytools.unittestframework.dll* and *microsoft.visualstudio.qualitytools.resource.dll*.

The steps are a little different when running under VSTS. You need to set up your Local Test Run settings to copy over your unmanaged dependencies. In order to do this, go to:

-   Test-&gt;Edit Test Run Configurations-&gt;Local Test Run
-   Click Deployment.Enter the dlls that you need copied over for each test:
    -   Wex.Logger.dll
    -   Wex.Common.dll
    -   Wex.Common.Managed.dll
    -   Wex.Communication.dll
    -   Wex.Logger.Interop.dll

This is necessary due to the fact that VSTS makes a new directory and copies files over every time that it runs your test cases. You can see these directories on your machine as sibling folder to your project folder.

## <span id="Running_managed_tests_in_the_default_application_domain"></span><span id="running_managed_tests_in_the_default_application_domain"></span><span id="RUNNING_MANAGED_TESTS_IN_THE_DEFAULT_APPLICATION_DOMAIN"></span>Running managed tests in the default application domain


By default, for test code isolation, TAEF executes managed tests in a special test application domain. However, when using non-default application domains, scenarios in which native code calls into managed code (e.g. native callback functions consumed by the managed code) can cause errors with the message: "Cannot pass a GCHandle across AppDomains". For these scenarios, force managed tests to run in the default application domain by using the [/defaultAppDomain](te-exe-command-line-parameters.md#defaultappdomain) switch.

Note that running managed tests in the default application domain is incompatible with [Assembly Config Files](assembly-config-files.md).

## <span id="Support_for_async_test_methods"></span><span id="support_for_async_test_methods"></span><span id="SUPPORT_FOR_ASYNC_TEST_METHODS"></span>Support for async test methods


TAEF's NetFX 4.5 binaries support the execution of async TAEF test methods. This means that TAEF tests that are marked with the **async** keyword are able to **await** async operations.

**Note**  Do not attempt to leverage this functionality with TAEF's NetFX 2.0/3.5 binaries; only the NetFX 4.5 binaries support this feature.

 

TAEF supports both async **void** and async **Task** test methods (both will result in the same functionality):

```CSharp
            [TestMethod]
            public async Task MyAsyncTest()
            {
                await AsyncAPICall1();
                var result = await AsyncAPICall2();
                Verify.IsTrue(result);
            }
```

Alternatively:

```CSharp
            [TestMethod]
            public async void MyAsyncTest2()
            {
                await AsyncAPICall1();
                var result = await AsyncAPICall2();
                Verify.IsTrue(result);
            }
```

 

 





