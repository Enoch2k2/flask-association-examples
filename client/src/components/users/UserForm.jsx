import React, { useEffect } from 'react'
import * as yup from "yup"
import {useFormik} from "formik"

const UserForm = ({ addUser, setError }) => {

  useEffect(() => {
    return () => {
      setError(null)
    }
  }, [])

  const formSchema = yup.object().shape({
    username: yup.string().required("username must exist").min(3).max(20)
    // email: yup.string().email("Invalid email"),
    // name: yup.string().required("Must enter a name").max(15),
    // age: yup.number().positive().integer().required("Must enter age").typeError('Please enter an Integer').max(125),
  })



  const formik = useFormik({
    initialValues: {
      username: "",
    },
    validationSchema: formSchema,
    onSubmit: submitUser
  });

  function submitUser(values) {
    fetch('/api/users', {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(values, null, 2)
    })
      .then(resp => resp.json())
      .then(data => addUser(data))
  }

  return (
    <form onSubmit={ formik.handleSubmit }>
      <h1>Create User</h1>
      <div>
        <label htmlFor="username">Username: </label>
        <input type="text" name="username" id="username" values={ formik.values.username } onChange={ formik.handleChange } />
        <p style={{ color: 'red' }}>{formik.errors.username}</p>
      </div>

      <input type="submit" value="Create User" />
    </form>
  )
}

export default UserForm