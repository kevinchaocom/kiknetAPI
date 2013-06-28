'''

The kiknet API

The python API for the kiknet database exposes these functions.
All functions returns a list of list. Where each individual list contains data for a single ground-motion record.

:copyright: (c) 2013 by Shrey K. Shahi, Haitham Dawood, and Adrian Rodriguez-Marek
:license: MIT, see LICENCE for more details.

'''

def paramEquals(paramName, paramValue, paramsRequested = [], filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where the *paramName* parameter is equal to *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The value that paramName must equal.
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramEquals('Mw',7.0)
        [{'gmNo':1, 'Mw':7.0, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw == 7.0
        >>> paramEquals('Mw',7.0,['Mw','Repi'])
        [{'Mw':7.0 , 'Repi':10.0}, ... ,{.....}] # Only Mw and Repi for all ground motions with Mw == 7.0
        >>> paramEquals('Mw',7.0,['*'])
        [{'gmNo':1, 'Mw':7.0, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0 ......}, .... , {............}] # All available parameters for all ground motions with Mw == 7.0
        
    '''

    return []

def paramLessThan(paramName, paramValue, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value less than *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The method will only return the data for records where paramName < paramValue
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramLessThan('Mw',7.0)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw < 7.0
        >>> paramLessThan('Mw',7.0,[],False)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw < 7.0, including low signal to noise ground motions
    '''

    return []

def paramLessThanEquals(paramName, paramValue, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value less than or equal to *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The method will only return the data for records where paramName <= paramValue
    :type paramValue: float
    :param paramsRequested: A list of parameters that the function will return for each ground motion. The default value of this parameter (empty list) returns the ground-motion number, moment magnitude, epicentral distance, Rjb, Vs30, aftershock flag for each ground motion. A list with string '*' can be used to request all available metadata.
    :type paramsRequested: list(str)
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramLessThanEquals('Mw',7.0)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0}, .... , {.....}] # Info for all ground motions with Mw <= 7.0
        >>> paramLessThanEquals('Mw',7.0,['*'],False)
        [{'gmNo':1, 'Mw':6.9, 'Repi':10.0, 'Rjb':8.0, 'Vs30':760.0, 'ASflag':0, ............}, .... , {............}] # All available parameters for all ground motions with Mw <= 7.0, including low signal to noise ground motions.
    '''
    
    return []

def paramGreaterThan(paramName, paramValue, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground motion in the database where the *paramName* parameter takes a value greater than *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The method will only return the data for records where paramName > paramValue
    :type paramValue: float
    :param paramsRequested: A comma separated list of parameters that the function will return for each ground motion. The default value of this parameter (empty string) returns .... for each ground motion. The string '*' can be used to request all available metadata.
    :type paramsRequested: str
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramEquals('Mw',7.0)
        [{.....},{.....}]
        >>> paramEquals('Mw',7.0,'Mw,Repi')
        [{.....},{.....}]
    '''

    return []

def paramGreaterThanEquals(paramName, paramValue, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where the *paramName* parameter takes a value greater than or equal to *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramValue: The method will only return the data for records where paramName <= paramValue
    :type paramValue: float
    :param paramsRequested: A comma separated list of parameters that the function will return for each ground motion. The default value of this parameter (empty string) returns .... for each ground motion. The string '*' can be used to request all available metadata.
    :type paramsRequested: str
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramEquals('Mw',7.0)
        [{.....},{.....}]
        >>> paramEquals('Mw',7.0,'Mw,Repi')
        [{.....},{.....}]
    '''

    return []

def paramInRange(paramName, paramRange, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where the *paramName* parameter takes a value within the range *paramValue*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramName: Name of the parameter used to filter the records.
    :type paramName: str
    :param paramRange: A string following the format 'lowerLimit to upperLimit', where lowerLimit and upperLimit are real numbers. The method will only return the data for records where paramName is within the paramRange.
    :type paramValue: str
    :param paramsRequested: A comma separated list of parameters that the function will return for each ground motion. The default value of this parameter (empty string) returns .... for each ground motion. The string '*' can be used to request all available metadata.
    :type paramsRequested: str
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    Usage:
        >>> paramEquals('Mw',7.0)
        [{.....},{.....}]
        >>> paramEquals('Mw',7.0,'Mw,Repi')
        [{.....},{.....}]
    '''

    return []

def multiParamsInRange(paramNames, paramRanges, paramsRequested = '', filterNoisy = True):
    '''
    Returns the values of the requested parameters for each ground-motion in the database where each parameter in the *paramNames* variable takes a value within the ranges defined by *paramValues*. A list of dictionaries is returned by the function, where each dictionary contains the different parameter:value pairs for each ground motion.

    :param paramNames: A comma seperated string of the names of the parameters used to filter the records.
    :type paramName: str
    :param paramRanges: A comma seperated string of following the format 'lowerLimit1 to upperLimit1 , lowerLimit2 to upperLimit2 , ... , lowerLimitN to upperLimitN', where lowerLimits and upperLimits are real numbers. The method will only return the data for records where paramName is within the paramRange.
    :type paramValue: str
    :param paramsRequested: A comma separated list of parameters that the function will return for each ground motion. The default value of this parameter (empty string) returns .... for each ground motion. The string '*' can be used to request all available metadata.
    :type paramsRequested: str
    :param filterNoisy: The default True value for this boolean switch removes all low signal to noise ratio records from the result. Passing False will include noisy signals in the results.
    :type filterNoisy: bool

    .. note::
        The i\ :sup:`th` parameter in paramNames will be checked to be withing the i\ :sup:`th` range in the paramRanges variable

    Usage:
        >>> paramEquals('Mw',7.0)
        [{.....},{.....}]
        >>> paramEquals('Mw',7.0,'Mw,Repi')
        [{.....},{.....}]
    '''

    return []

def spectraForGmNos(gmNo, periods = [-1] , components = []):
    '''
    Returns the 5% damped linear elastic response spectra for the list of ground motions specified by *gmNo* variable. The spectra is returned in a dictionary which contain the componentName:spectra pairs. componentName can take one of the following values:
        
        #. S1 - EW component of the surface record.
        #. S2 - NS component of the surface record.
        #. S3 - Vertical component of the surface record.
        #. B1 - EW component of the borehole record.
        #. B2 - NS component of the borehole record.
        #. B3 - Vertical component of the borehole record.

    The spectra for each component is represent by a list of list. Where each individual list contains the spectral ordinates for each ground motion. The spectral values follow the order of the periods in the *periods* variable. Also the spectra lists follow the order of ground motions in the *gmNo* list.

    :param gmNo: A list of ground-motion numbers for which the spectra is needed.
    :type gmNo: list(int)
    :param periods: A list of periods at which the spectra is computed. The default value is a list with -1 as the first element, this results in spectra being calculated at T = .... , a list with -2 as first element returns.
    :type periods: list(float)
    :param components: A list of components for which the spectra is needed. The user select any combination of S1, S2, S3, B1, B2, B3. The meaning of these names are described in the list above. The default value of this parameter is an empty list, which returns the EW and NS components of the surface motion.
    :type components: list(str)
    '''

    return []