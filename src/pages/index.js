import React from 'react';

import PropTypes from 'prop-types';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import { withStyles } from 'material-ui/styles';
import withRoot from '../withRoot';
import Grid from 'material-ui/Grid';
import Paper from 'material-ui/Paper';
import Avatar from 'material-ui/Avatar';
import IconButton from 'material-ui/IconButton';
import KeyboardArrowUp from '@material-ui/icons/KeyboardArrowUp';
import KeyboardArrowDown from '@material-ui/icons/KeyboardArrowDown';
import TextField from 'material-ui/TextField';
import AddIcon from '@material-ui/icons/Add';
import Button from 'material-ui/Button';





const styles = theme => ({
  root: {
    overflow: 'hidden',
    padding: `0 ${theme.spacing.unit}px`,
  },
  wrapper: {
    maxWidth: 800,
    justify: 'center',
  },
  paper: {
    margin: theme.spacing.unit,
    padding: theme.spacing.unit * 2,
  },
  vote_cnt: {
    display: 'inline'
  },
  textField: {
    margin: theme.spacing.unit,
    width: 700,
  }
});

class Index extends React.Component {
  state = {
    topics: [],
    topicContent: '',
  };

  fetchTopics = () => {
    fetch('/topics')
      .then(response => response.json())
      .then(data => this.setState({ topics: data }));
  }

  createTopic = () => {
    fetch(`/topics`, {
      method: 'post',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        'content': this.state['topicContent']
      }),
    })
      .then((data) => {
        this.fetchTopics()
      });
  }

  handleUpVote = (id, event) => {
    fetch(`/topics/${id}/action/1`, { method: 'put' })
      .then(response => response.json())
      .then((data) => {
        this.fetchTopics()
      });
  };

  handleDownVote = (id, event) => {
    fetch(`/topics/${id}/action/2`, { method: 'put' })
      .then(response => response.json())
      .then((data) => {
        this.fetchTopics()
      });
  };

  handleChangeTopicContent = (event) => {
    this.setState({ topicContent: event.target.value })
  };

  handleSubmitTopic = (event) => {
    this.createTopic()
  };

  handleKeyDown = (event) => {
    let keycode = (event.keyCode ? event.keyCode : event.which);
    console.log(keycode)
    if (keycode === 13) {
      this.createTopic()
    }
  };

  componentDidMount = () => {
    this.fetchTopics()
  };

  render() {
    const { classes } = this.props;
    let topics = this.state.topics.map(topic => {
      return <Paper className={classes.paper} key={topic.id}>
        <Grid container wrap="nowrap" spacing={16}>
          <Grid item>
            <Avatar>T</Avatar>
          </Grid>
          <Grid item xs>
            <Typography>{topic.content}</Typography>
            <IconButton aria-label="Upvote" onClick={this.handleUpVote.bind(this, topic.id)}>
              <KeyboardArrowUp />
            </IconButton>
            <Typography className={classes.vote_cnt}>{topic.result}</Typography>
            <IconButton aria-label="Downvote" onClick={this.handleDownVote.bind(this, topic.id)}>
              <KeyboardArrowDown />
            </IconButton>
            <Typography>Upvotes: {topic.upvote}</Typography>
            <Typography>Downvotes: {topic.downvote}</Typography>
          </Grid>
        </Grid>
      </Paper>
    })
    return (
      <div className={classes.root}>
        <AppBar position="static" color="primary">
          <Toolbar>
            <Typography variant="title" color="inherit">
              Coding Exercise
            </Typography>
          </Toolbar>
        </AppBar>
        <TextField
          label="Topic"
          value={this.state.topicContent}
          onChange={this.handleChangeTopicContent}
          onKeyDown={this.handleKeyDown}
          className={classes.textField}
          margin="normal"
        />
        <Button variant="fab" mini color="primary" aria-label="add" className={classes.button} onClick={this.handleSubmitTopic}>
          <AddIcon />
        </Button>
        <div className={classes.wrapper}>
          {topics}
        </div>
      </div>
    );
  }
}

Index.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withRoot(withStyles(styles)(Index));
