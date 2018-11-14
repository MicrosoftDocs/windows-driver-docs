---
title: Making the Most of TAEF
description: Making the Most of TAEF
ms.assetid: DCB06C5A-DF2C-4e1c-A297-C9AA5496D162
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Making the Most of TAEF


Test Authoring and Execution Framework provides you with a powerful platform to author and execute your tests. It might be beneficial to understand some behind the scenes functioning details of TAEF in order to make the most of it. This page discusses some tips and features that will help you author your tests to optimize and make the most of what TAEF has to offer. Please make sure that you are familiar with the basics of Authoring and Executing tests with TAEF.

## <span id="Set-up__or_Initialize__and_Clean-up_Methods"></span><span id="set-up__or_initialize__and_clean-up_methods"></span><span id="SET-UP__OR_INITIALIZE__AND_CLEAN-UP_METHODS"></span>Set-up (or Initialize) and Clean-up Methods


The setup and cleanup methods at the assembly level (also known as *fixtures*), get run once per DLL execution. Similarly the class level setup and cleanup methods get run once per class. The test level setup and cleanup methods are the same for all the tests within a class, and are invoked once before and after every test in the class.

There may only be one assembly level setup and cleanup method per assembly, one class level setup and cleanup method per class, and one test setup and cleanup method per class. Note that class setup and cleanup methods are static in managed code, but are not static in C++ code.

If exceptions are enabled (the default case), the execution of any method is terminated on the first Verify call that fails. If you have explicitly disabled exception-based Verify calls (see the Verify section in Authoring Tests for details), you will need to have explicit conditional statements to govern the control flow after a Verify call fails.

In the case where the failure happens in a Setup method (either by way of exception based verify failure or by setup explicitly returning a failure), the tests that were to follow are considered "Blocked" and logged as such. For example, if your Class level Setup method fails, all the test methods in the Class are considered "Blocked" and each of them will be logged as such. In addition to that, the Cleanup method won't be invoked if the failure happens in a Setup method.

## <span id="Test_Method"></span><span id="test_method"></span><span id="TEST_METHOD"></span>Test Method


It is not required to explicitly log the test result. If all Verify calls in your test succeeded, the test will be logged as "Passed". On the first Verify call that fails, the test method execution will terminate (unless you have explicitly disabled exception based Verify calls - in which case your conditional statements will determine the control flow there after but regardless the following holds) and the test will be marked as "Failed".

Similarly, if you have a VERIFY (depends on the return type and what determines success) wrapper around a helper method invocation call, you won't need to explicitly check and log its result.

## <span id="Specifying_Metadata"></span><span id="specifying_metadata"></span><span id="SPECIFYING_METADATA"></span>Specifying Metadata


Metadata lookup is hierarchical. This means if your select statement is **/select:"@Priority=2"**, and if your TestMethod does not specify Priority, TAEF will look up at the class that contains it. If the Class level metadata does not specify it, TAEF looks up at the assembly level.

So, if you want all or most of the tests in your class to have the same "Priority", or say "Owner, you can get that by just specifying it at the class level. For the one or few tests that are an exception to this rule, you can explicitly provide the metadata at the "TestMethod" level. See the following test for details:

```cpp
1    namespace WEX { namespace UnitTests { namespace Samples
2    {
3        //
4        // Declare module level properties
5        //
6        BEGIN_MODULE() //This metadata applies to all the classes and tests in this module or assembly
7            MODULE_PROPERTY(L"GroupOwner", L"SomeGroup")
8        END_MODULE()
9        class PremiumBankAccountTests
10       {
11           //
12           // Declare this class to be a test class with an&#39;advanced&#39; declaration
13           // Use advanced declaration when you want to set metadata on the class
14           //
15           BEGIN_TEST_CLASS(PremiumBankAccountTests) //This metadata applies to all the test in this class
16               TEST_CLASS_PROPERTY(L"Priority", L"2")
17               TEST_CLASS_PROPERTY(L"DevOwner", L"Someone")
18               TEST_CLASS_PROPERTY(L"PMOwner", L"Someone")
19           END_TEST_CLASS()
20           //
21           // Declare class setup - a method that runs after class constructor
22           // and before any test class methods and test setup method
23           //
24           TEST_CLASS_SETUP(SetDefaultAccountType);
25           //
26           // Declare class cleanup - a methods that runs after all the class test methods and test setup method
27           // and before the class destructor
28           //
29           TEST_CLASS_CLEANUP(ResetDefaultAccountType);
30           //
31           // Declare test setup and cleanup - methods that run before and after the execution
32           // of every test method correspondingly
33           //
34           TEST_METHOD_SETUP(CreateBankAccount);
35           TEST_METHOD_CLEANUP(DestroyBankAccount);
36           //
37           // Declare test methods with an &#39;advanced&#39; declaration
38           // Use advanced declaration when you want to set metadata on the methods
39           //
40           BEGIN_TEST_METHOD(DebitTest)
41               TEST_METHOD_PROPERTY(L"BVT", L"TRUE")
42               TEST_METHOD_PROPERTY(L"PERF", L"TRUE")
43               TEST_METHOD_PROPERTY(L"STRESS", L"FALSE")
44               TEST_METHOD_PROPERTY(L"Priority", L"1") //Overrides the Class level Priority value
45           END_TEST_METHOD()
46           BEGIN_TEST_METHOD(CreditTest)
47               TEST_METHOD_PROPERTY(L"BVT", L"TRUE")
48               TEST_METHOD_PROPERTY(L"PERF", L"FALSE")
49               TEST_METHOD_PROPERTY(L"STRESS", L"TRUE")
50               TEST_METHOD_PROPERTY(L"GroupOwner", L"SomeGroupTest") //Overrides the GroupOwner specified at the Module level
51           END_TEST_METHOD()
52   
53           std::unique_ptr<BankAccount> m_spBankAccount;
54           BankAccountType m_defaultType;
55       };
56   } /* namespace Samples */ } /* namespace UnitTests */ } /* namespace WEX */
```

NOTE: For managed tests, the authoring is done similarly. Module level is the same as Assembly level markup in managed. ***For Assembly level or Class level metadata specification in managed code, the markup has to be provided before the static Initializer methods.*** This may mean that you may have to provide an empty Initializer if your test doesn't already have one. This design is specifically crafted to ensure VSTS compatibility.

In case of table based data-driven tests you can take this a step further and override test level metadata by specifying it at the Row level. See [Metadata Overriding Data Driven Test Example](metadata-overriding-data-driven-test-example.md) for details.

 

 





