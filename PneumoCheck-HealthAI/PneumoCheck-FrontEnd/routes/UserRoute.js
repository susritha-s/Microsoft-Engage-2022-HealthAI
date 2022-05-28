import { useEffect, useState } from "react";
import axios from "axios";
import { useRouter } from "next/router";
import { makeStyles } from '@material-ui/core/styles';
import LinearProgress from '@material-ui/core/LinearProgress';

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
    '& > * + *': {
      marginTop: theme.spacing(2),
    },
  },
}));

// wrapping several routes
//to pass down the children for further process.
const UserRoute = ({ children, showNav = true }) => {
  
  // declaring state
  const [ok, setOk] = useState(false);
// Declaring router and classes
  const router = useRouter();
  const classes = useStyles();

//creating function to fetch the user 
  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = async () => {
    try {
      const { data } = await axios.get("/api/current-user");
      //   console.log(data);
      if (data.ok) setOk(true);
    } catch (err) {
      console.log(err);
      setOk(false);
      router.push("/login");
    }
  };

  return (
    <>
      {!ok ? (
        <div className={classes.root}>
          <LinearProgress />
        </div>
      ) : (
        <div >
          <div >
            <div >{children}</div>
          </div>
        </div>
      )}
    </>
  );
  };


export default UserRoute;
