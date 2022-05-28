import React from 'react';


import { useRouter } from "next/router";
import ArrowRightAltIcon from '@material-ui/icons/ArrowRightAlt';
import { Typography, IconButton } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import clsx from 'clsx';
import PropTypes from 'prop-types';



//******Basic Styling */
const useStyles = makeStyles(theme => ({
  root: {
    display: 'inline-flex',
    alignItems: 'center',
    textDecoration: 'none',
  },
  title: {
    fontWeight: 'bold',
  },
  icon: {
    padding: 0,
    marginLeft: theme.spacing(1),
    '&:hover': {
      background: 'transparent',
    },
  },
}));

/**
 * Component to display the "Read More About Pnuemomia" link
 *
 * @param {Object} props
 */
const LearnMoreLinkPlain = props => {
  const {
    color,
    component,
    variant,
    title,
    href,
    className,
    iconProps,
    typographyProps,
    ...rest
  } = props;

  const classes = useStyles();
  const router = useRouter();


  const children = (
    <>
      <Typography
        component="span"
        className={clsx('learn-more-link__typography', classes.title)}
        variant={variant}
        color={color || 'primary'}
        {...typographyProps}
      >
        {title}
      </Typography>
      <IconButton
        className={clsx('learn-more-link__icon-button', classes.icon)}
        color={color || 'primary'}
        {...iconProps}
      >
        <ArrowRightAltIcon className="learn-more-link__arrow" />
      </IconButton>
    </>
  );

  return (
    <a
      className={clsx('learn-more-link', classes.root, className)}
      {...rest}
    >
      {children}
    </a>
  );
};

LearnMoreLinkPlain.defaultProps = {
  variant: 'subtitle1',
  href: '#',
  typographyProps: {},
  iconProps: {},
  component: 'a',
};

LearnMoreLinkPlain.propTypes = {
 
  className: PropTypes.string,
  
  component: PropTypes.oneOf(['Link', 'a']),
  
  title: PropTypes.string.isRequired,
  
  variant: PropTypes.oneOf(['h6', 'subtitle1', 'subtitle2', 'body1', 'body2']),
  
  href: PropTypes.string,
  
  color: PropTypes.string,
  
  iconProps: PropTypes.object,
  
  typographyProps: PropTypes.object,
};

export default LearnMoreLinkPlain;
