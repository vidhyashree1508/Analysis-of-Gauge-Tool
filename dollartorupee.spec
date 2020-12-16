# Dollar to rupee spec

This spec is to test the function that converts dollar to rupee
This specification also tests some functions with respect to unicode values

## Dollar to rupee

tags: conversion

This spec tests the conversion value from dollars to rupees 

* The conversion of "10" dollars to rupee is "740"

## Dollar to rupee symbols

tags: unicode_compliance_runner

* The dollar symbols should be the same for the "$" and the unicode value


## Passing Unicode value as a parameter

tags: unicode_compliance

* This tests that the unicode value "\u0024" is passed correctly from gauge to the runner and it prints "$"

