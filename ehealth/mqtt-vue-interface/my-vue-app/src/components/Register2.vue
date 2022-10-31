<ul id="tabs-swipe-demo" class="tabs">
  <li class="tab col s3 blue-text">
    <a class="active indigo white-text" href="#test-swipe-1"
      >Registrarse como paciente</a
    >
  </li>
  <li class="tab col s3">
    <a class="purple white-text" href="#test-swipe-2"
      >Registrarse como doctor</a
    >
  </li>
</ul>


<div id="test-swipe-2" class="col s12 white row">
    <div>
      <br />

      <div class="container">
        <div class="col s12 container" id="post-form">
          <div class="row">
            <div class="col s12">
              <div class="row">
                <div class="input-field col s12">
                  <input
                    placeholder="Ingrese una titulacion o diplomado que posea"
                    id="rd_title"
                    type="text"
                    class="validate"
                    v-model="state.title"
                  />
                  <h6 class="red white-text" v-if="v$.title.$error">
                    {{ v$.title.$errors[0].$message }}
                  </h6>
                </div>

                <div class="col s12">
                  <div class="row">
                    <div class="input-field col s12">
                      <input
                        placeholder="Cedula de doctor"
                        id="rd_id"
                        type="text"
                        class="validate"
                        v-model="state.dcc"
                      />
                      <h6 class="red white-text" v-if="v$.dcc.$error">
                        {{ v$.dcc.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Nombre "
                        id="rd_name"
                        type="text"
                        class="validate"
                        v-model="state.dname"
                      />
                      <h6 class="red white-text" v-if="v$.dname.$error">
                        {{ v$.dname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Segundo nombre"
                        id="rd_sname"
                        type="text"
                        class="validate"
                        v-model="state.dsname"
                      />
                      <h6 class="red white-text" v-if="v$.dsname.$error">
                        {{ v$.dsname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Apellido"
                        id="rd_lastname"
                        type="text"
                        class="validate"
                        v-model="state.dlname"
                      />
                      <h6 class="red white-text" v-if="v$.dlname.$error">
                        {{ v$.dlname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Segundo apellido"
                        id="rd_slastname"
                        type="text"
                        class="validate"
                        v-model="state.dslname"
                      />
                      <h6 class="red white-text" v-if="v$.dslname.$error">
                        {{ v$.dslname.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="input-field col s12">
                      <input
                        placeholder="Fecha de nacimiento"
                        id="rd_bdate"
                        type="date"
                        class="validate"
                        v-model="state.dbd"
                      />
                      <label for="first_name">Fecha de nacimiento</label>
                      <h6 class="red white-text" v-if="v$.dbd.$error">
                        {{ v$.dbd.$errors[0].$message }}
                      </h6>
                    </div>

                    <div class="center">
                      <button
                        onclick="register_doctor()"
                        class="btn purple darken-4"
                        name="doctor"
                        type="submit"
                      >
                        Registrarse
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>