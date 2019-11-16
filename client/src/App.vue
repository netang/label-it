<template>
  <div id="app">
    <div class="row">
      <div class="col-md-7">
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="col">Имя разметки</th>
              <th scope="col">Описание</th>
              <th scope="col">Инициатор</th>
              <th scope="col">Прогресс</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="task in tasks" :key="task.id">
              <th>{{task.name}}</th>
              <td><pre>{{task.description}}</pre></td>
              <td>{{task.initiator}}</td>
              <td>{{task.progress}}</td>
              <td><button class="btn btn-primary btn-sm mb-1">Перейти</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "main",
  data: function() {
    return {
      tasks: null
    };
  },
  methods: {
    get_tasks: function() {
      axios
        .get("http://127.0.0.1:5000/api/tasks/")
        .then(response => (this.tasks = response.data.tasks))
        .catch(error => (console.error(error)));
    }
  },
  mounted() {
    this.get_tasks();
  }
};

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-left: 60px;
  margin-right: 60px;
}
</style>
