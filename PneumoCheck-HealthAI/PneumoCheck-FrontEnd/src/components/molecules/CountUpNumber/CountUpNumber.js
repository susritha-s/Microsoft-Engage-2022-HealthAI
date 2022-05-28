import React from 'react';

import PropTypes from 'prop-types';
import VisibilitySensor from 'react-visibility-sensor';
import CountUp from 'react-countup';
import clsx from 'clsx';
import { Typography } from '@material-ui/core';

/**
 * ******This component is used to display the count
 *
 * @param {Object} props
 */
const CountUpNumber = props => {
  const {
   
    labelColor,
    className,
    visibilitySensorProps,
    wrapperProps,
    countWrapperProps,
    countNumberProps,
    labelProps,
    start,
    end,
    suffix,
    prefix,
    label,
    textColor,
    ...rest
  } = props;

  const [viewPortEntered, setViewPortEntered] = React.useState(false);
  const setViewPortVisibility = isVisible => {
    if (viewPortEntered) {
      return;
    }

    setViewPortEntered(isVisible);
  };

  return (
    <div className={clsx('countup-number', className)} {...rest}>
      <VisibilitySensor
        onChange={isVisible => setViewPortVisibility(isVisible)}
        delayedCall
        {...visibilitySensorProps}
      >
        <div className="countup-number__wrapper" {...wrapperProps}>
          <Typography
            variant="h4"
            gutterBottom
            align="center"
            color={textColor || 'textPrimary'}
            className="countup-number__count-wrapper"
            {...countWrapperProps}
          >
            <CountUp
              delay={1}
              redraw={false}
              end={viewPortEntered ? end : start}
              start={start}
              suffix={suffix || ''}
              prefix={prefix || ''}
              className="countup-number__count"
              {...countNumberProps}
            />
          </Typography>
          <Typography
            variant="subtitle1"
            color={labelColor || 'textSecondary'}
            align="center"
            className="countup-number__label"
            {...labelProps}
          >
            {label}
          </Typography>
        </div>
      </VisibilitySensor>
    </div>
  );
};

CountUpNumber.defaultProps = {
  start: 0,
  visibilitySensorProps: {},
  wrapperProps: {},
  countWrapperProps: {},
  countNumberProps: {},
  labelProps: {},
};

CountUpNumber.propTypes = {
 
  className: PropTypes.string,
 
  suffix: PropTypes.string,
  
  prefix: PropTypes.string,
  
  label: PropTypes.string.isRequired,
 
  start: PropTypes.number,
  
  end: PropTypes.number.isRequired,
  
  textColor: PropTypes.string,
  
  labelColor: PropTypes.string,

  visibilitySensorProps: PropTypes.object,
 
  wrapperProps: PropTypes.object,
 
  countWrapperProps: PropTypes.object,
  
  countNumberProps: PropTypes.object,
  
  labelProps: PropTypes.object,
};

export default CountUpNumber;
