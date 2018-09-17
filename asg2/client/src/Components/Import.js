import React from 'react'
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';

class Import extends React.Component {

  state ={
    indicator_id: '',
    response: '0',
    res: {}
  }

  onChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    })
  }

  async onSubmit(e) {
    e.preventDefault();
    // const res = await axios.get(`http://api.worldbank.org/v2/countries/all/indicators/${this.state.indicator_id}?date=2012:2017&format=json&per_page=100`)
    // console.log("woohoo...",res.data);
    const res = [{"page":2,"pages":32,"per_page":50,"lastupdated":"2018-08-28","total":1584},[{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"Z7","value":"Europe & Central Asia"},"countryiso3code":"","date":"2015","value":20373360511263.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"Z7","value":"Europe & Central Asia"},"countryiso3code":"","date":"2014","value":23658228163840.5,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"Z7","value":"Europe & Central Asia"},"countryiso3code":"","date":"2013","value":23352202041538.8,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"Z7","value":"Europe & Central Asia"},"countryiso3code":"","date":"2012","value":22343569115289.3,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"7E","value":"Europe & Central Asia (excluding high income)"},"countryiso3code":"","date":"2017","value":3300500740186.92,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"7E","value":"Europe & Central Asia (excluding high income)"},"countryiso3code":"","date":"2016","value":2943297166689.13,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"7E","value":"Europe & Central Asia (excluding high income)"},"countryiso3code":"","date":"2015","value":3074852612469.76,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"7E","value":"Europe & Central Asia (excluding high income)"},"countryiso3code":"","date":"2014","value":4021783448232.2,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"7E","value":"Europe & Central Asia (excluding high income)"},"countryiso3code":"","date":"2013","value":4311458738453.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"7E","value":"Europe & Central Asia (excluding high income)"},"countryiso3code":"","date":"2012","value":4054552441559.32,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"T7","value":"Europe & Central Asia (IDA & IBRD countries)"},"countryiso3code":"","date":"2017","value":3879859485679.2,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"T7","value":"Europe & Central Asia (IDA & IBRD countries)"},"countryiso3code":"","date":"2016","value":3466035965437.18,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"T7","value":"Europe & Central Asia (IDA & IBRD countries)"},"countryiso3code":"","date":"2015","value":3601633743536.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"T7","value":"Europe & Central Asia (IDA & IBRD countries)"},"countryiso3code":"","date":"2014","value":4624592551758.33,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"T7","value":"Europe & Central Asia (IDA & IBRD countries)"},"countryiso3code":"","date":"2013","value":4893778917069.39,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"T7","value":"Europe & Central Asia (IDA & IBRD countries)"},"countryiso3code":"","date":"2012","value":4611478733661.98,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"EU","value":"European Union"},"countryiso3code":"","date":"2017","value":17277697660475,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"EU","value":"European Union"},"countryiso3code":"","date":"2016","value":16491855791194.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"EU","value":"European Union"},"countryiso3code":"","date":"2015","value":16416670356766.4,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"EU","value":"European Union"},"countryiso3code":"","date":"2014","value":18635535561984.7,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"EU","value":"European Union"},"countryiso3code":"","date":"2013","value":18029679886231.6,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"EU","value":"European Union"},"countryiso3code":"","date":"2012","value":17292774157162.6,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"F1","value":"Fragile and conflict affected situations"},"countryiso3code":"","date":"2017","value":830726810714.623,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"F1","value":"Fragile and conflict affected situations"},"countryiso3code":"","date":"2016","value":724091067411.028,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"F1","value":"Fragile and conflict affected situations"},"countryiso3code":"","date":"2015","value":758948867366.725,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"F1","value":"Fragile and conflict affected situations"},"countryiso3code":"","date":"2014","value":854436872033.342,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"F1","value":"Fragile and conflict affected situations"},"countryiso3code":"","date":"2013","value":844211308436.993,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"F1","value":"Fragile and conflict affected situations"},"countryiso3code":"","date":"2012","value":812460412982.903,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XE","value":"Heavily indebted poor countries (HIPC)"},"countryiso3code":"","date":"2017","value":728774036366.636,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XE","value":"Heavily indebted poor countries (HIPC)"},"countryiso3code":"","date":"2016","value":652175948756.265,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XE","value":"Heavily indebted poor countries (HIPC)"},"countryiso3code":"","date":"2015","value":640013775850.345,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XE","value":"Heavily indebted poor countries (HIPC)"},"countryiso3code":"","date":"2014","value":650445161954.419,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XE","value":"Heavily indebted poor countries (HIPC)"},"countryiso3code":"","date":"2013","value":612898760943.11,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XE","value":"Heavily indebted poor countries (HIPC)"},"countryiso3code":"","date":"2012","value":564381508746.692,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XD","value":"High income"},"countryiso3code":"","date":"2017","value":51475414395949.6,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XD","value":"High income"},"countryiso3code":"","date":"2016","value":49281856158945.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XD","value":"High income"},"countryiso3code":"","date":"2015","value":48322414816705.8,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XD","value":"High income"},"countryiso3code":"","date":"2014","value":51048743606969,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XD","value":"High income"},"countryiso3code":"","date":"2013","value":50012560794420.7,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XD","value":"High income"},"countryiso3code":"","date":"2012","value":49467213807435.4,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XF","value":"IBRD only"},"countryiso3code":"","date":"2017","value":28648517074135.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XF","value":"IBRD only"},"countryiso3code":"","date":"2016","value":26025458644283.5,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XF","value":"IBRD only"},"countryiso3code":"","date":"2015","value":25892267158724,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XF","value":"IBRD only"},"countryiso3code":"","date":"2014","value":27417808169925.2,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XF","value":"IBRD only"},"countryiso3code":"","date":"2013","value":26548453670328.9,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"XF","value":"IBRD only"},"countryiso3code":"","date":"2012","value":25110781711224.5,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"ZT","value":"IDA & IBRD total"},"countryiso3code":"","date":"2017","value":30741796092143.4,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"ZT","value":"IDA & IBRD total"},"countryiso3code":"","date":"2016","value":28005663818401.2,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"ZT","value":"IDA & IBRD total"},"countryiso3code":"","date":"2015","value":27915726843475.4,"unit":"","obs_status":"","decimal":0},{"indicator":{"id":"NY.GDP.MKTP.CD","value":"GDP (current US$)"},"country":{"id":"ZT","value":"IDA & IBRD total"},"countryiso3code":"","date":"2014","value":29510452511451,"unit":"","obs_status":"","decimal":0}]]
    console.log(res);
    const res1 = await axios.post('http://localhost:5000/indicators',res)
    console.log("woohoo...",res1.data);
    this.setState({res: res1.data, response:'1'})

  }

  render () {
    if (this.state.response === 1) {
      return (
        <div>got git</div>
      )
    }
    else {
      return(
        <form onSubmit={this.onSubmit.bind(this)}>
          <TextField
            label="Indicator ID"
            name="indicator_id"
            value={this.state.indicator_id}
            onChange={this.onChange.bind(this)}
            margin="normal"
          />
          <Button
                type="submit"
                color="primary"
              >Import
              </Button>
        </form>
      )
    }

  }
}

export default Import;
