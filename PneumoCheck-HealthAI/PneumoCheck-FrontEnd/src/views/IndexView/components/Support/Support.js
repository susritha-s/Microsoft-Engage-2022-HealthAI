import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import {
  useMediaQuery,
  Grid,
  ListItem,
  ListItemAvatar,
  Typography,
  Avatar,
  colors,
} from '@material-ui/core';
import { SectionHeader, IconAlternate } from '../../../../components/molecules';

const useStyles = makeStyles(theme => ({
  listItemAvatar: {
    minWidth: 28,
  },
  listItem: {
    [theme.breakpoints.up('sm')]: {
      justifyContent: 'center',
    },
  },
  galleryMedia: {
    width: 80,
    height: 80,
    marginLeft: theme.spacing(-2),
    border: `3px solid ${theme.palette.background.paper}`,
    '&:first-child': {
      marginLeft: 0,
    },
    [theme.breakpoints.up('sm')]: {
      width: 100,
      height: 100,
    },
    [theme.breakpoints.up('md')]: {
      width: 140,
      height: 140,
    },
  },
}));

const Contact = props => {
  const { data, className, ...rest } = props;
  const classes = useStyles();

  const { items, team } = data;

  const theme = useTheme();
  const isMd = useMediaQuery(theme.breakpoints.up('md'), {
    defaultMatches: true,
  });

  return (
    <div className={className} {...rest}>
      <Grid container spacing={isMd ? 4 : 2}>
        <Grid item xs={12}>
          <SectionHeader
            
            title={
              <>
                <span>
                  How To Use 
                  <Typography color="secondary" variant="inherit" component="span">
                    {' '}
                    PneumoCheck
                  </Typography>
                </span>
              </>
            }
            subtitle="You need to register yourself first by clicking on the Register button on top right.
            Then, Login Using your credentials. Click on Predict on the top right and then upload the image
            of the chest x-ray to be detected. The Results along with the accuracy will be displayed on the screen
            within a few seconds."
            
            align="center"
            disableGutter
          />
          </Grid>
          </Grid>
      </div>
        
         
   
  );
};

Contact.propTypes = {
  /**
   * External classes
   */
  className: PropTypes.string,
  /**
   * Data to render
   */
  data: PropTypes.object.isRequired,
};

export default Contact;
