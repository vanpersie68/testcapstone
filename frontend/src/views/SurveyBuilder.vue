<template>
  <!-- for PC -->
  <div id="app" v-if="PageType">
    <!-- <the-tool-bar /> -->
    <div class="editor-content" v-if="survey.currentPage === 'editor'">
      <the-panel-base :editorData="survey.editorData" />
      <the-work-space />
    </div>

    <div class="flow-content" v-if="survey.currentPage === 'flow'">
      <the-flow-editor />
      <div class="button-row bottom-row">
        <button-base class="secondary standard" :title="'Cancel'" />
        <button-base class="primary standard" :title="'Save'" />
      </div>
    </div>
  </div>
  <!-- for mobile -->
  <div id="app" v-else>
    <div id='testtt'></div>
    <!-- <the-tool-bar /> -->
    <div class="editor-content" v-if="survey.currentPage === 'editor'">
      <the-panel-base-m-b :editorData="survey.editorData" />
      <the-work-space />
    </div>

    <div class="flow-content" v-if="survey.currentPage === 'flow'">
      <the-flow-editor />
      <div class="button-row bottom-row">
        <the-panel-base-m-b :editorData="survey.editorData" />
        <button-base class="secondary standard" :title="'Cancel'" />
        <button-base class="primary standard" :title="'Save'" />
      </div>
    </div>
  </div>
</template>


<script>
import TheToolBar from '../components/SurveyBuilder/TheToolBar.vue'
import ThePanelBase from '../components/SurveyBuilder/ThePanelBase.vue'
import ThePanelBaseMB from '../components/SurveyBuilder/ThePanelBaseForMobile.vue'
import TheWorkSpace from '../components/SurveyBuilder/TheWorkSpace.vue'
import store from '../store/SurveyBuilder'
import TheFlowEditor from '../components/SurveyBuilder/TheFlowEditor.vue'
import ButtonBase from '../components/ButtonBase.vue'
import { relativeTimeRounding } from 'moment'

export default {
  name: 'SurveyBuilder',
  store: store,
  data() {
    return {
      // Page Type:PC/Mobile
      PageType: true,
      // Record the size of the screen
      screenWidth: null,
      // Flag for reload
      render: true
    }
  },
  watch: {},
  mounted() {
    // When initialization, get the screen width
    window.addEventListener('load', this.checkWidth)
    //If the window size hange, reload the page
    window.addEventListener('resize', this.checkWidth)
    window.addEventListener('resize', this.reload)
  },
  destroyed() {
    window.removeEventListener('resize', this.reload)
  },
  methods: {
    // Reload the page
    reload() {
      this.render = false
      this.$nextTick(() => {
        this.render = true
      })
    },
    // Check the screen width
    checkWidth() {
      this.screenWidth = document.body.clientWidth
      console.log("screenwidth:" + this.screenWidth)
      if (this.screenWidth < 766) {
        this.PageType = false;
      }
      else {
        this.PageType = true;
      }
    }
  },
  components: {
    TheToolBar,
    ThePanelBase,
    ThePanelBaseMB,
    TheWorkSpace,
    TheFlowEditor,
    ButtonBase,
  },
  async created() {
    store.dispatch('loadSurvey', this.$route.params.id)
  },
  computed: {
    survey() {
      return store.getters['wholeSurvey']
    },
  },
}
</script>

<style scoped>
/* TODO: fix up rtl button styling */
html:lang(ur) * {
  text-align: right;
}

#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 0px;
  width: 100%;
  /* height: calc(100vh - 112px); */
  overflow: hidden;
}

.editor-content {
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  width: 100%;
  max-height: calc(100vh - 56px);
  min-height: calc(100vh - 56px);
  /* max-height: calc(100% - 112px); */
  overflow: hidden;
}

.button-row {
  display: flex;
  flex-direction: row;
  /* padding: 16px 0; */
  align-items: center;
}

.bottom-row {
  position: sticky;
  bottom: 0;
  left: 0;
  background-color: white;
  width: 100%;
  justify-content: flex-end;
  border-top: 1px solid #566370;
}
</style>
